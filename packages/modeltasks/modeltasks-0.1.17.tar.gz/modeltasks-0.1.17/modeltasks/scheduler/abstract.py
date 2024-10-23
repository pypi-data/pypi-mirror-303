import os
import sys
from time import sleep
from textwrap import shorten
from logging import Logger
from pathlib import Path
from typing import Dict, List, Union, Any, Callable, ValuesView
from modeltasks.log import TaskLogger
from modeltasks.task import ModelTask
from modeltasks.util.task import ExecutionTimer
from modeltasks.scheduler.job import JobPipeline
from modeltasks.handler.abstract import EventHandler


class AbstractScheduler:
    """
    A generic scheduler functioning as template class for
    writing Schedulers. A scheduler should must be able to queue
    tasks (producer) for distinct submodels and trigger workers
    (consumers) which will concurrently execute those tasks. A scheduler
    needs to be provided with one or more job plans (which are a disaggregated
    submodel = graph of dependant tasks). Such a job plan is a sequence of
    configured jobs (task instances), which have to be either run
    sequentially or when possible run simultaneously.
    """

    _scheduler = None
    _workers: List = None
    _pipelines: Dict = None
    _pending: List = None
    _processed: Dict = None
    _done: Any = None
    _failed: Any = None
    _use_cache: bool = None
    _concurrent: bool = False
    _workspace: Path = None
    _cache: Path = None
    _logger: Logger = None
    _events: EventHandler = None
    _strict_invalidation: bool = None

    @property
    def concurrent(self):
        return self._concurrent

    @property
    def workspace(self):
        return self._workspace

    @workspace.setter
    def workspace(self, path: Path):
        self._workspace = path

    @property
    def cache(self):
        return self._cache

    @cache.setter
    def cache(self, path: Path):
        self._cache = path

    @property
    def pipelines(self) -> ValuesView[JobPipeline]:
        return self._pipelines.values()

    @property
    def job_count(self) -> int:
        return sum([len(p) for p in self.pipelines]) if self.pipelines else 0

    def __init__(
        self,
        run_concurrent: bool = False,           # Can tasks be executed concurrently
        use_cache: bool = True,                 # Use the caching system
        workspace: Path = None,                 # Workspace path for task processes
        logger: Logger = None,                  # The logger used by the task scheduler
        handler: EventHandler = None,           # An Event handler class
        strict_invalidation: bool = False       # Should we run all subsequent tasks again when one task ran?
    ):
        self._workers = []
        self._pipelines = {}
        self._processed = {}
        self._pending = []
        self._concurrent = bool(run_concurrent)
        self._use_cache = bool(use_cache)
        self._workspace = workspace
        self._logger = logger
        self._events = handler or EventHandler()
        self._strict_invalidation = strict_invalidation

    def schedule(self, jobs: List[List], pipeline: Union[int, str] = None):
        """
        Schedule jobs in a pipeline. If pipeline does not exists, then it will be created.
        """

        # Reset the done event
        self._done = False

        # Enqueue jobs to pipeline
        pipeline = self._pipelines.setdefault(pipeline or 'default', JobPipeline())
        pipeline.add(jobs)

    def run(self, use_cache: bool = None, handler: EventHandler = None):
        """
        Execute the scheduled tasks (blocking until all tasks are done)
        """

        # Configure cache usage
        if use_cache is not None:
            self._use_cache = use_cache

        # Configure event handler
        if handler:
            self._events = handler

        # Update handlers with pipelines
        self._events.pipelines = list(self._pipelines.values())

        # Start the scheduler
        try:
            self._events.on_model_start()
        except Exception as e:
            self._logger.error(f'Event handler error for model invocation ({e})')
        self._start_scheduler()

    def _start_scheduler(self):
        """
        The template method responsible for starting the scheduler
        """

        # Start the scheduler
        if not self._scheduler:
            self._scheduler = True
            self._process_jobs()

    def jobs_done(self):
        self._done = True

    def get_pipeline(self, pipeline: Union[str, int]) -> JobPipeline:
        """
        Return a specific pipeline
        """
        return self._pipelines.get(pipeline)

    def _process_jobs(self):
        """
        The template method responsible to schedule & process jobs from the pipelines
        """

        def on_executed(task: ModelTask):
            pass

        def on_failed(task: ModelTask, error: Exception):
            self.jobs_done()

        for index, pipeline in self._pipelines.items():
            if not pipeline.paused and not pipeline.lock:
                for job in pipeline.get():
                    if not self.execute_job(
                        job,
                        on_executed,
                        on_failed
                    ):
                        break

        self.jobs_done()

    def abort_job(
        self,
        job: Dict,
        error_message: str,
        on_failed: Callable = None,
        error: Exception = None
    ):
        """
        A routine to abort the job execution.
        """
        # Set this task as failed
        task = job.get('instance')
        self._failed = task.name

        # Log error
        if error_message:
            self._logger.error(error_message)

        # Call a provided task failure handler method (so for instance a subclass specific method)
        if on_failed:
            on_failed(task, error or RuntimeError(error_message))

        # Notify the event handler
        try:
            self._events.on_task_failed(task, error_message)
        except Exception as e:
            self._logger.error(f'Event handler error for failed task "{task.name}" ({error_message})')

    def execute_job(
        self,
        job: Dict,
        on_job_executed: Callable,
        on_job_failed: Callable,
        executor: str = None
    ):
        """
        Executes a task instance and is responsible for resolving dependencies into actual result values.
        Also checks if all outputs are set, etc. And marks a task as completed when done.
        """

        # A simple tuple put into the job queue will tell workers to quit
        if job is False:
            return False

        # Get task instance
        task = job.get('instance')
        start = job.get('start')
        end = job.get('end')

        if task.name not in self._processed:
            # Add task name immediately to indicate it is in progress (to avoid the identical job being triggered concurrently from another pipeline)
            self._processed.update({
                task.name: task
            })

            # Call event handler
            try:
                self._events.task_start(task)
            except Exception as e:
                self._logger.error(f'Event handler error for starting task "{task.name}" ({e})')

            # Configure task with input values (which can be looked up from outputs of already processed jobs)
            if not start:
                for i in task.get_inputs():
                    input_variable = getattr(task, i)
                    output_variable = None
                    required_task_id, required_output_name = input_variable.dependency
                    try:
                        required_task = self._processed[required_task_id]
                    except KeyError:
                        self.abort_job(
                            job,
                            f'Task dependencies cannot be fulfilled for task "{task.name}" (Required task "{required_task_id}" was not yet processed)',
                            on_failed=on_job_failed
                        )
                        sys.exit()
                    try:
                        output_variable = getattr(required_task, required_output_name)
                    except AttributeError:
                        self.abort_job(
                            job,
                            f'Cannot resolve input "{required_task_id}.{required_output_name}" for task "{task.name}" (Wrong variable name "{required_output_name}"?)',
                            on_failed=on_job_failed
                        )
                        sys.exit()
                    if not output_variable.is_set:
                        self.abort_job(
                            job,
                            f'Input variable "{required_output_name}" for task "{task.name}" is None (Forgot to set value for "{required_output_name}" in task "{required_task_id}"?)',
                            on_failed=on_job_failed
                        )
                        sys.exit()
                    else:
                        setattr(task, i, output_variable)

            # Set the RUN flag by default to `True` and then make tests if we really need to run the task
            run = True

            # Check if all of the tasks's outputs already exist in the cache and if yes and in case we can use them, skip the processing!
            if self._use_cache:
                # Check result cache only if task allows result caching
                if task.cache_results is True:

                    # Check if this task has any untracked (static) inputs. In case, then we need to run this task
                    count_untracked = sum([
                        len([i for i in task.get_inputs() if getattr(task, i).untracked is True]),
                        len([p for p in task.get_parameters() if getattr(task, p).untracked is True])
                    ])
                    if count_untracked > 0:
                        run = True
                    else:
                        # If any of the task's outputs is not cached, we need to run the task anyway
                        # This also catches the case for instance for folder/file-based output
                        # that got changed by a user/process and leads to new hashes
                        run = not all([getattr(task, o).is_cached(self.cache) for o in task.get_outputs()])

                # Do some extra checks if we need to run the task even if all outputs exits in the cache
                if run is False:
                    # With strict invalidation of cached results, we need to run the task if any prior task ran
                    if self._strict_invalidation and any([self._processed[getattr(task, i).dependency[0]].ran for i in task.get_inputs()]):
                        run = True

            # Load task outputs from cache if we do not need to run the task
            if self._use_cache and run is False:
                for output in [getattr(task, o) for o in task.get_outputs()]:
                    if output.cacheable:
                        self._logger.debug(f'==> Reading now cached value for output: {task.name}.{output.id}')
                        output.deserialize(self.cache)
                        self._logger.info(f'''Task "{task.name}": Found cached model output "{output.id}" = {shorten(
                            str(output.value),
                            width=150,
                            placeholder="..."
                        )}''')
                        # Check if deserialized value can be used (If not we can stop here and run the task again)
                        if output.value is None:
                            # This might happen when files and folders were changed or if cached results can't be read
                            self._logger.warning(f'Task "{task.name}": Could not use cached output "{output.id}" (Need to run task again)')
                            run = True
                            break
                if run is False:
                    self._logger.info(f'Task "{task.name}": Using cached results')

            # Run the task (There are several reasons why a task might eventually run again. Check conditions above)
            if self._use_cache is False or run is True:
                with ExecutionTimer(name=task.name, logger=self._logger, executor=executor, failed=self._failed):
                    try:
                        # Capture the current working path
                        cwd = Path.cwd()

                        # Run the task
                        task.run(TaskLogger(self._logger, task.name), workspace=self.workspace)

                        # On task finished
                        task.on_finished(TaskLogger(self._logger, task.name), workspace=self.workspace)
                    except Exception as e:
                        # Abort job
                        self.abort_job(
                            job,
                            f'Task "{task.name}": Failed to run task because of "{type(e).__name__}" ({e})',
                            on_failed=on_job_failed
                        )
                    finally:
                        # Show output results
                        for output in [getattr(task, o) for o in task.get_outputs()]:
                            if output.is_set:
                                self._logger.info(f'''Task "{task.name}": Task output "{output.id}" = {shorten(
                                    str(output.value),
                                    width=150,
                                    placeholder="..."
                                )}''')

                        # Ensure that all output values have their value set and warn if a task produced no output!
                        output_check = [(o, not getattr(task, o).is_set) for o in task.get_outputs()]
                        if any([missing for o, missing in output_check]) is True:
                            self.abort_job(
                                job,
                                f'''Task "{task.name}": The following mandatory task outputs were not set (Outputs: {", ".join(
                                    [o for o, missing in output_check if missing]
                                )})''',
                                on_failed=on_job_failed
                            )

                        # Write outputs to cache (if caching is enabled, if task succeeded and allows caching)
                        if self._use_cache and self._failed != task.name:
                            if task.cache_results:
                                for output in [getattr(task, o) for o in task.get_outputs()]:
                                    if output.cacheable and output.is_set:
                                        try:
                                            self._logger.debug(f'==> Writing now output to cache: {task.name}.{output.id}')
                                            output.serialize(self.cache)
                                        except Exception as e:
                                            self.abort_job(
                                                job,
                                                f'Task "{task.name}": Failed to write output "{output.id}" to cache "{self.cache}" ({e})',
                                                on_failed=on_job_failed
                                            )
                            else:
                                self._logger.info(f'Task "{task.name}": Result caching disabled by task')

                        # Ensure that working dir does not get changed
                        os.chdir(cwd)

                        # Mark the task as ran
                        task.ran = True

            # If jobs successfully ran
            if self._failed != task.name:
                task.processed = True

                # Call a provided callback
                on_job_executed(task)

                # Call event handler
                try:
                    self._events.task_done(task)
                except Exception as e:
                    self._logger.error(f'Event handler error for finished task "{task.name}" ({e})')

                # Handle final results
                if end:
                    for output in [getattr(task, o) for o in task.get_outputs()]:
                        self._logger.info(f'''Final model output "{task.name}.{output.id}" = {shorten(
                            str(output.value),
                            width=150,
                            placeholder="..."
                        )}''')

                    # Call event handler
                    try:
                        self._events.on_model_results([getattr(task, o) for o in task.get_outputs()])
                    except Exception as e:
                        self._logger.error(f'Event handler error for model results "{task.name}" ({e})')

                    # Signal that all scheduled jobs are complete
                    self.jobs_done()
                return True
            else:
                return False

        else:
            # This task is in process. Let's check if it is already completed and if not wait for its completion
            processed_task = self._processed.get(task.name)
            if processed_task.processed:
                self._logger.info(f'Task "{task.name}": Already processed (Skipping task)')
            else:
                self._logger.info(f'Task "{task.name}": Currently being processed (Waiting for its completion ...)')
                while True:
                    if processed_task.processed is True:
                        break
                    sleep(0.5)
            try:
                on_job_executed(task)
            finally:
                return True
