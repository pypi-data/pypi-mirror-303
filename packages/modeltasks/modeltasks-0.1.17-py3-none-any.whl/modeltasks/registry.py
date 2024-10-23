import sys
import logging
import importlib.util
from typing import Type, List, Union, Dict, Any
from pathlib import Path
from dataclasses import dataclass
from modeltasks.log import logger
from modeltasks.task import ModelTask, ModelTaskMount
from modeltasks.data import TaskInput, TaskOutput
from modeltasks.config import TaskParameter


@dataclass
class RegistryTask:
    name: str = None
    instance: Type[ModelTask] = None
    inputs: Dict = None
    outputs: Dict = None
    parameters: Dict = None


@dataclass
class RegistryTaskInput:
    dependency: str = None
    name: str = None
    type: str = None
    module: str = None
    raw: Any = None


@dataclass
class RegistryTaskOutput:
    type: str = None


@dataclass
class RegistryTaskParameter:
    type: Type[TaskParameter] = None
    key: str = None
    options: str = None


class TaskRegistry(metaclass=ModelTaskMount):
    """
    Serves as a central registry for all model task classes
    """

    # Tasks
    _tasks: Dict = {}
    _modules: List = []
    _current_import = None

    # The default path of tasks
    _task_path = None

    def __init__(self, task_path: Path = None):
        # Load from specified tasks path
        self.load_task_path(task_path=task_path)

    def load_task_path(self, task_path: Path = None):
        """
        Loads tasks from the registries task path or optionally loads tasks from the specified source
        """
        if task_path and task_path == self.__class__.get_task_path():
            pass
        elif not task_path:
            # Reset existing registry
            self.__class__._tasks = {}
        self.__class__.set_task_path(task_path)

        # Load tasks from path
        self.__class__._current_import = None
        self.__class__._load_tasks()

        # Try to correct any unresolved task dependencies once all tasks have been loaded
        self.__class__._resolve_missing_dependencies()

        # Check if all related inputs and outputs actually match by there type
        self.__class__._check_io_match()

        # If DEBUG is true, then print the registered tasks
        self._list_tasks()

    def get_task(self, task: str) -> Union[RegistryTask, None]:
        return self.__class__._tasks.get(task, None)

    def get_tasks(self) -> List:
        return self.__class__._get_tasks()

    def get_task_names(self) -> List:
        return self.__class__._get_task_names()

    def reset_registry(self):
        self.__class__._tasks = {}
        self.__class__._modules = []


    def _list_tasks(self):
        # Debug code
        if logger.level == logging.DEBUG:
            for t, d in self.__class__._tasks.items():
                logger.info(f'{(t + " ").ljust(30, "=")}> {d}')
                for i, ti in d.inputs.items():
                    logger.info(f'   {"|_ INPUT":15} {i} == {ti.dependency} ({ti.type})')
                for i, ti in d.outputs.items():
                    logger.info(f'   {"|_ OUTPUT":15} {i} == ? ({ti.type})')
                for i, ti in d.parameters.items():
                    logger.info(f'   {"|_ PARAMETER":15} {i} == {ti.key} ({ti.type})')

    @classmethod
    def _get_tasks(cls) -> List:
        return [task for name, task in cls._tasks.items()]

    @classmethod
    def _get_task_names(cls) -> List:
        return [name for name, task in cls._tasks.items()]

    @classmethod
    def set_task_path(cls, task_path: Path):
        if task_path:
            if task_path and not Path(task_path).exists():
                logger.error(f'Provided task path "{task_path}" does not exist or is not a file or directory')
                raise FileNotFoundError(f'Task registry path "{task_path}" does not exist')
            cls._task_path = task_path
        else:
            cwd_tasks = Path.cwd() / 'model'
            script_tasks = Path(sys.argv[0]).parent / 'model'
            if cwd_tasks.exists():
                cls._task_path = cwd_tasks
                logger.warning(f'Using default task path "{cwd_tasks}" (Specify other if not correct)')
            elif script_tasks.exists():
                logger.warning(f'Using default task path "{script_tasks}" (Specify other if not correct)')
                cls._task_path = script_tasks

    @classmethod
    def get_task_path(cls) -> Union[None, Path]:
        return cls._task_path

    @classmethod
    def _load_tasks(cls):
        """
        Loads and registers tasks from a path of Python modules
        """
        modules = [cls._task_path] if cls._task_path.is_file() else list(cls._task_path.rglob('*.py'))
        for p in modules:
            module = p.name
            if module != '__init__.py':
                cls._current_import = module
                if module not in cls._modules:
                    logger.info(f'Loading model tasks from module "{module}"')
                    cls._modules.append(module)
                    spec = importlib.util.spec_from_file_location(p.stem, p)
                    try:
                        logger.debug(f'Importing from module "{p}"')
                        spec.loader.exec_module(importlib.util.module_from_spec(spec))
                    except Exception as e:
                        logger.warning(f'Failed to import from module "{p}" ({type(e).__name__}: {e})')
                else:
                    logger.debug(f'Module "{module}" already imported (Avoid recursive imports in your model)')
        if len(cls._tasks) == 0:
            logger.warning(f'Found 0 task from task source "{cls._task_path}" (Task path correctly set?)')
            sys.exit()

    @classmethod
    def _check_io_match(cls):
        """
        Checks if related inputs and outputs have the same IO type.
        This is another check to be sure a task output is of the same type as the input
        of a dependent task.
        """
        logger.info('Checking IO type match between tasks')
        for t, n, i in [(t.name, n, i) for t in cls._tasks.values() for n, i in t.inputs.items()]:
            input_class = i.type
            try:
                output_class = cls._tasks[i.dependency].outputs[i.name].type
            except KeyError:
                logger.error(f'Task "{i.dependency}" does not have an output "{i.name}" as required by task "{t}" (Check task definition)')
                sys.exit()
            try:
                if input_class._type != output_class._type:
                    logger.error(f'Type of input "{n}" in task "{t}" does not match output "{i.name}" of task "{i.dependency}" ({input_class._type} != {output_class._type})')
                    sys.exit()
            except AttributeError:
                if not hasattr(input_class, '_type'):
                    logger.error(f'Input "{n}" class has no IO type defined (Update class "{type(output_class)}" with a "_type" attribute)')
                elif not hasattr(output_class, '_type'):
                    logger.error(f'Output "{i.name}" class has no IO type defined (Update class "{type(output_class)}" with a "_type" attribute)')
                sys.exit()

    @classmethod
    def _resolve_missing_dependencies(cls):
        """
        Resolves all missing task dependencies after all tasks have been registered and their outputs can be looked up
        """
        logger.info('Resolving task dependencies')
        task_instances = {n: t.instance for n, t in cls._tasks.items()}

        for t, n, i in [(t.name, n, i) for t in cls._tasks.values() for n, i in t.inputs.items() if not i.name or not i.dependency]:
            name = i.name or None
            dependency = i.dependency or None
            if not dependency:
                if i.raw in task_instances:
                    dependency = cls._lookup_dependency(task_instances.get(i.raw), t, i.module)
                elif (task_id := f'{i.module}.{i.raw}') in task_instances:
                    dependency = cls._lookup_dependency(task_instances.get(task_id), t, i.module)
                elif '.' in i.raw and (task_id := f'{i.module}.{i.raw[0:i.raw.rindex(".")]}') in task_instances:
                    dependency = cls._lookup_dependency(task_instances.get(task_id), t, i.module)
                else:
                    dependency = cls._lookup_dependency(i.raw, t, i.module)
            if not name:
                name = cls._lookup_output(task_instances.get(dependency or i.raw), t, n, i.module, raw=i.raw)
            if name:
                i.name = name
            if dependency:
                i.dependency = dependency

        # Make a last check and warn user if not all dependencies could be resolved
        unresolved = [(t.name, n, i) for t in cls._tasks.values() for n, i in t.inputs.items() if not i.name or not i.dependency]
        if len(unresolved) > 0:
            for t, n, i in unresolved:
                logger.error(f'Task dependency "{n}" is unresolved (Correct or specify non-ambiguous dependency in task "{t}")')
                sys.exit()

    @classmethod
    def _lookup_output(cls, output: Union[str, ModelTask], task_name: str, task_input: str, task_module: str, raw: str = None) -> str:
        try:
            if issubclass(output, ModelTask):
                outputs = output.get_outputs()
                if len(outputs) == 0:
                    logger.error(f'Task "{task_name}" depends on task "{output.get_task_name()}" which has no outputs (Properly annotated outputs in "{output.get_task_name()}"?)')
                    sys.exit()
                elif len(outputs) > 1:
                    if raw and raw.split('.')[-1] in outputs:
                        return raw.split('.')[-1]
                    else:
                        logger.error(f'Task "{task_name}" requires ambiguous output from task "{output.get_task_name()}" (Specify exact task output for input "{task_input}")')
                        sys.exit()
                else:
                    return outputs[0]
        except TypeError:
            if isinstance(output, ModelTask):
                outputs = output.__class__.get_outputs()
                if len(outputs) == 0:
                    logger.error(f'Task "{task_name}" depends on task "{output.get_task_name()}" which has no outputs (Properly annotated outputs in "{output.get_task_name()}"?)')
                    sys.exit()
                elif len(outputs) > 1:
                    if raw and raw.split('.')[-1] in outputs:
                        return raw.split('.')[-1]
                    else:
                        logger.error(f'Task "{task_name}" requires ambiguous output from task "{output.name}" (Specify exact task output for input "{task_input}")')
                        sys.exit()
                else:
                    return outputs[0]
        if output:
            registered_tasks = cls._get_task_names()
            if '.' in output and output[0:output.rindex('.')] in registered_tasks:
                return output[output.rindex('.') + 1:]
            elif '.' in output and output[0:output.rindex('.')] in [r.split('.')[-1] for r in registered_tasks]:
                return output[output.rindex('.') + 1:]
            else:
                return False
        else:
            logger.warning(f'Required task input "{task_input}" is not properly specified. Update input in task "{task_name}"')

    @classmethod
    def _lookup_dependency(cls, requirement: Union[str, ModelTask, type], task_name: str, task_module: str) -> str:
        try:
            if issubclass(requirement, ModelTask):
                return cls.get_task_id(requirement.get_task_name())
        except TypeError:
            if isinstance(requirement, ModelTask):
                return cls.get_task_id(requirement.name)
        if requirement:
            registered_tasks = cls._get_task_names()
            if '.' in requirement:
                if '.' in requirement and requirement[0:requirement.rindex('.')] in registered_tasks:
                    return requirement[0:requirement.rindex('.')]
                # elif '.' in requirement and requirement[0:requirement.rindex('.')] in [r.split('.')[-1] for r in registered_tasks]:
                #     return f'{task_module}.{requirement[0:requirement.rindex(".")]}'
                else:
                    return False
            else:
                # if requirement in [r.split('.')[-1] for r in registered_tasks]:
                #     return f'{task_module}.{requirement}'
                # else:
                return False
        else:
            logger.warning(f'Found unknown task input dependency in module "{task_name}"')
            return 'Unknown'

    @classmethod
    def get_task_id(cls, task) -> str:
        task_name = task if isinstance(task, str) else task.get_task_name()
        task_folder = cls._task_path.name + '.'
        return task_name.split(task_folder)[-1]

    @classmethod
    def register_task(cls, task):
        # We do not register tasks from the main module as we cannot control when we load them or when they get defined
        if task.__module__ == '__main__':
            return
        # Register task
        try:
            if (task_id := cls.get_task_id(task)) not in cls._tasks:
                logger.info(f'Registering model task "{task_id}"')

                task = task(task_id=task_id)
                inputs = {}
                outputs = {}
                parameters = {}

                try:
                    for a_name, a_type in task.__annotations__.items():
                        try:
                            if issubclass(a_type, TaskInput):
                                inputs.update({
                                    a_name: RegistryTaskInput(
                                        dependency=cls._lookup_dependency(
                                            getattr(task, a_name),
                                            task_name=task.name,
                                            task_module=task.__module__
                                        ),
                                        name=cls._lookup_output(
                                            getattr(task, a_name),
                                            task_name=task.name,
                                            task_input=a_name,
                                            task_module=task.__module__
                                        ),
                                        type=a_type,
                                        module=task.__module__,
                                        raw=getattr(task, a_name)
                                    )
                                })
                            elif issubclass(a_type, TaskOutput):
                                outputs.update({
                                    a_name: RegistryTaskOutput(
                                        type=a_type
                                    )
                                })
                            elif issubclass(a_type, TaskParameter):
                                parameter_attribute = getattr(task, a_name)
                                parameter_key = parameter_attribute.split('[')[0]
                                parameter_options = parameter_attribute.split('[')[1][0:-1] if '[' in parameter_attribute else None
                                parameters.update({
                                    a_name: RegistryTaskParameter(
                                        type=a_type,
                                        key=parameter_key,
                                        options=parameter_options
                                    )
                                })
                        except ModuleNotFoundError:
                            logger.error(f'Missing task dependency: Cannot find model task "{getattr(task, a_name)}" specified in "{task_id}"')
                            sys.exit()
                        except Exception as e:
                            logger.error(f'Failed to interpret properties of task "{task_id}" ({e})')
                            sys.exit()

                except AttributeError:
                    pass

                cls._tasks[task_id] = RegistryTask(
                    name=task_id,
                    instance=task,
                    inputs=inputs,
                    outputs=outputs,
                    parameters=parameters
                )
        except Exception as e:
            logger.warning(f'Failed to register model task "{cls.get_task_id(task)}" ({type(e).__name__}: {e})')

    @classmethod
    def unregister_task(cls, task):
        try:
            if (task_id := cls.get_task_id(task)) in cls._tasks:
                logger.info(f'Unregistering model task "{task_id}"')
                del cls._tasks[task_id]
        except Exception as e:
            logger.error(f'Failed to unregister task "{cls.get_task_id(task)}" ({type(e).__name__}: {e})')
