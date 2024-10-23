from modeltasks.task import ModelTask
from modeltasks.data import TaskOutput
from modeltasks.scheduler.job import JobPipeline
from typing import List, Union, Dict


class EventHandler:
    """
    An abstract handler class that can be subclassed to implement custom model or task event handling.
    The default implementation already keeps track of ongoing tasks and model progress.
    """

    _pipelines: List[JobPipeline] = None
    _job_processing: Dict = {}
    _job_total: int = 0
    _job_finished: int = 0

    @property
    def pipelines(self) -> Union[None, List[JobPipeline]]:
        return self._pipelines

    @pipelines.setter
    def pipelines(self, pipelines: List[JobPipeline]):
        self._pipelines = pipelines
        self._job_total = sum([len(pipeline.list()) for pipeline in self._pipelines])

    @property
    def job_count(self) -> int:
        return self._job_total - self._job_finished

    @property
    def job_active(self) -> List[ModelTask]:
        return self._job_processing.values()

    @property
    def job_progress(self) -> float:
        if self._job_total != 0 and self._job_total == self._job_finished:
            return 1.0
        else:
            return round(self._job_finished / self._job_total, 2) if self._job_total != 0 else 0.0

    def task_start(self, task):
        self._job_processing[task.name] = task
        self.on_task_start(task)

    def task_done(self, task):
        del self._job_processing[task.name]
        self._job_finished += 1
        self.on_task_end(task)

    def on_task_start(self, task: ModelTask):
        """When a task is executed"""
        pass

    def on_task_end(self, task: ModelTask):
        """When a task has finished"""
        pass

    def on_task_failed(self, task: ModelTask, failure: Exception):
        """When a task execution has failed"""
        pass

    def on_tasks_loaded(self, tasks: List[ModelTask]):
        """When all tasks have been loaded and validated"""
        pass

    def on_tasks_scheduled(self, tasks: List[ModelTask]):
        """When tasks have been scheduled"""
        pass

    def on_model_start(self):
        """When the task scheduler is started"""
        pass

    def on_model_failed(self):
        """When a model execution has failed"""
        pass

    def on_model_results(self, outputs: List[TaskOutput]):
        """When a task is cancelled"""
        pass

    def on_model_end(self):
        """When a model was completed"""
        pass
