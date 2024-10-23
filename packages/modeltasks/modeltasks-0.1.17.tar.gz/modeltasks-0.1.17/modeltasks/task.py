import logging
from typing import Any
from pathlib import Path
from modeltasks.log import logger
from modeltasks.config import TaskParameter
from modeltasks.data import TaskInput, TaskOutput
from modeltasks.util.hash import get_hash


class ModelTaskMount(type):
    """
    A metaclass which handles the registration of all model tasks.
    Acts as a middleman object between model tasks and the task registry.
    """

    register = None
    unregister = None

    def __init__(cls, name, bases, attributes):
        if hasattr(cls, 'register_task'):
            ModelTaskMount.register = cls.register_task
            ModelTaskMount.unregister = cls.unregister_task
        else:
            if ModelTaskMount.register:
                ModelTaskMount.register(cls)


class ModelTask(metaclass=ModelTaskMount):
    """
    A template class to implement model tasks
    """

    _task_id: str = None
    _initialized: bool = False
    _processed: bool = False
    _ran: bool = False
    _hash: str = None
    _model: Any = None
    _cache_results: bool = True

    group: [str, None] = None

    @property
    def name(self) -> str:
        return self._task_id

    @property
    def initialized(self) -> bool:
        return self._initialized

    @property
    def processed(self) -> bool:
        return self._processed

    @processed.setter
    def processed(self, state: bool):
        self._processed = bool(state)

    @property
    def ran(self) -> bool:
        return self._ran

    @ran.setter
    def ran(self, state: bool):
        self._ran = bool(state)

    @property
    def hash(self) -> str:
        """
        Returns a task hash which is derived from the hashes of its parameters, inputs and its name.
        All outputs of this task will use this task hash to calculate their own hash. Therefor
        output hashes will change if the task hash changed due to new parameters or different inputs.
        """
        if not self._hash:
            parameter_hashes = [getattr(self, p).hash for p in sorted(self.get_parameters())]
            input_hashes = [getattr(self, i).hash for i in sorted(self.get_inputs())]
            self._hash = get_hash(f'{self.name}_{"".join(parameter_hashes + input_hashes)}')
        return self._hash

    @property
    def cache_results(self) -> bool:
        """
        Indicates on a task level if results of this task can be cached or not.
        By default, task results are cached if caching is enabled and if the task outputs
        are defined as cacheable. Setting a task as non-cacheable disables the caching for
        any of its results.
        """
        return self._cache_results

    def __init__(self, task_id: str = None):
        self._task_id = task_id or self.__class__.get_task_name()
        logger.debug(f'Initializing model task "{self.name}"')
        self._initialized = True

    def __repr__(self):
        return f'<ModelTask: {self.name}>'

    # def __getattribute__(self, attribute):
    #     if attribute == '__annotations__':
    #         return super().__getattribute__(attribute)
    #     else:
    #         # Check if we want to access a task parameter / input or output and
    #         if a_type := super().__getattribute__('__annotations__').get(attribute):
    #             is_cls_task_attribute = False
    #             if issubclass(a_type, TaskParameter):
    #                 is_cls_task_attribute = True
    #             elif issubclass(a_type, TaskOutput):
    #                 is_cls_task_attribute = True
    #             elif issubclass(a_type, TaskInput):
    #                 is_cls_task_attribute = True
    #             if is_cls_task_attribute:
    #                 variable = super().__getattribute__(attribute)
    #                 try:
    #                     return variable
    #                 except AttributeError:
    #                     pass
    #         return super().__getattribute__(attribute)

    def __setattr__(self, attribute, value):
        if a_type := super().__getattribute__('__annotations__').get(attribute):
            if issubclass(a_type, TaskOutput):
                # Handle task outputs
                try:
                    # Attribute already exists!
                    output = super().__getattribute__(attribute)
                    if hasattr(value, '_get_other_value'):
                        # Is or value another TaskVariable?
                        output.value = value.value
                    else:
                        # Is any other value
                        output.value = value
                except AttributeError:
                    # No output attribute exists!
                    if hasattr(value, '_get_other_value'):
                        # Is or value another TaskVariable?
                        super().__setattr__(attribute, value if isinstance(value, TaskOutput) else value.value)
                    else:
                        # Is any other value
                        super().__setattr__(attribute, TaskOutput(value))
            elif issubclass(a_type, TaskInput) or issubclass(a_type, TaskParameter):
                # Handle Task inputs or parameters
                try:
                    variable = super().__getattribute__(attribute)
                    if hasattr(variable, '_get_other_value') and variable.is_set:
                        # Attribute already exists and has a value (Don't change a set input or parameter twice!)
                        logger.warning(f'Task variable "{attribute}" is already configured with a value (Do not attempt to modify existing value)')
                    elif hasattr(variable, '_get_other_value'):
                        # Attribute already exists but is not set yet. Set the value but make sure only to use the value only and do not set another task variable
                        variable.value = value.value if hasattr(value, '_get_other_value') else value
                    else:
                        super().__setattr__(attribute, value)
                except AttributeError:
                    super().__setattr__(attribute, value)
            else:
                super().__setattr__(attribute, value)
        else:
            super().__setattr__(attribute, value)

    @classmethod
    def get_outputs(cls):
        return [n for n, t in cls.__annotations__.items() if issubclass(t, TaskOutput)]

    @classmethod
    def get_inputs(cls):
        return [n for n, t in cls.__annotations__.items() if issubclass(t, TaskInput)]

    @classmethod
    def get_parameters(cls):
        return [n for n, t in cls.__annotations__.items() if issubclass(t, TaskParameter)]

    @classmethod
    def get_task_name(cls):
        return f'{cls.__module__}.{cls.__qualname__}'

    def run(self, logger: logging.LoggerAdapter, workspace: Path):
        logger.info(f'Running model task "{self.name}"')

    def on_finished(self, logger: logging.LoggerAdapter, workspace: Path):
        logger.info(f'Task done')
        # TODO: Display a list of the results of the task, so one can easily read the value or find the location on disk
        # for output in [(o, getattr(o, self)) for o in self.get_outputs()]:
        #     print('done')
        #     logger.info(f'Task "{self.name}" created output "{output[0]}"={o[1]}')
