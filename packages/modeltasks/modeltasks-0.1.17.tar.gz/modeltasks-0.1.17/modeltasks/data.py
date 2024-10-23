from pathlib import Path
from typing import Any, Tuple
from modeltasks.log import logger
from modeltasks.util.hash import (
    get_hash,
    get_file_hash,
    get_file_hash_checksum,
    get_folder_hash,
    get_folder_hash_checksum
)
from modeltasks.util.task import TaskVariable
from modeltasks.util.io import(
    serialize as serialize_value,
    deserialize as deserialize_value
)


class TaskIO:
    """
    A shared IO class working as a mixin that is used by both task inputs and outputs.
    Add here methods that are used by inputs and outputs
    """

    _id: str = None
    _task = None
    _cacheable: bool = True
    _untracked: bool = False
    _type: str = None

    @property
    def id(self) -> str:
        return self._id

    @property
    def identifier(self) -> str:
        return f'{self.task.name + "." if self.task else ""}{self.id}.{self.task.hash if self.task else self.hash}'

    @property
    def task(self):
        return self._task

    @property
    def cacheable(self) -> bool:
        return self._cacheable if not self._untracked else False

    @property
    def untracked(self) -> bool:
        return self._untracked

    def __init__(self, id: str = None, task=None, cacheable: bool = True, *args, **kwargs):
        self._id = id
        self._task = task
        self._cacheable = cacheable

    def serialize(self, cache: Path, value: Any = None):
        """
        Method to serialize the value of a task IO as JSON/Pickle to the cache
        """
        if self.cacheable:
            try:
                serialize_value(cache_file := cache / self.identifier, value or self.value)
            except ValueError:
                logger.warning(f'Could not cache value of "{self.task.name}.{self.id}" (Unsupported variable value)')
            finally:
                if cache_file.exists() and cache_file.stat().st_size == 0:
                    logger.warning(f'Could not cache value of "{self.task.name}.{self.id}" (Cache file is empty)')

    def deserialize(self, cache: Path):
        """
        Method to deserialize the value of a task IO from a JSON/Pickle
        """
        if self.cacheable:
            try:
                self.value = deserialize_value(cache_file := cache / self.identifier)
            except FileNotFoundError:
                logger.warning(
                    f'Cannot find cached result "{cache_file}" for "{self.task.name}.{self.id}" (Cache file does not exist)')
            finally:
                if self.value is None:
                    logger.warning(f'Could not read cached value of "{self.task.name}.{self.id}" (Unsupported variable value)')

    def is_cached(self, cache: Path) -> bool:
        """
        Method to check if a cached value of this IO exists in the specified cache folder
        """
        try:
            return (cache / self.identifier).exists() if self.cacheable else False
        except:
            return False


class TaskInput(TaskIO, TaskVariable):
    """
    The template class for defining the inputs of a task
    """

    _dependency: Tuple = None

    @property
    def dependency(self) -> Tuple:
        return self._dependency

    def __init__(self, *args, id: str = None, task=None, cacheable: bool = True, dependency: Tuple = None, **kwargs):
        TaskIO.__init__(self, id, task, cacheable)
        TaskVariable.__init__(self, *args, **kwargs)
        self._dependency = dependency


class TaskOutput(TaskIO, TaskVariable):
    """
    The template class for defining outputs of a task
    """

    def __init__(self, *args, id: str = None, task=None, cacheable: bool = True, **kwargs):
        TaskIO.__init__(self, id, task, cacheable)
        TaskVariable.__init__(self, *args, **kwargs)


class StaticInput(TaskInput):
    """
    A static input that represents a value (for instance a string, integer, float, etc)
    It will always return the same hash based on its name, not its value and therefore does
    not affect a task's hash if its value changes
    """

    _type = 'static_variable'
    _untracked = True

    def _get_hash(self) -> str:
        return get_hash(f'{self.task.name + "." if self.task else ""}{self.id}')


class StaticOutput(TaskOutput):
    """
    A static output that represents a variable (for instance a string, integer, float, etc).
    It will always return the same hash based on its name, not its value and therefore does
    not affect a task's hash if its value changes
    """

    _type = 'static_variable'
    _untracked = True

    def _get_hash(self) -> str:
        return get_hash(f'{self.task.name + "." if self.task else ""}{self.id}')


class VariableInput(TaskInput):
    """
    A variable input that represents a variable (for instance a string, integer, float, etc)
    """

    _type = 'variable'

    def _get_hash(self) -> str:
        return get_hash(self._value)


class VariableOutput(TaskOutput):
    """
    A variable output that represents a variable (for instance a string, integer, float, etc)
    """

    _type = 'variable'

    def _get_hash(self) -> str:
        return get_hash(self._value)


class FileInput(TaskInput):
    """
    An input representing a file based process input
    Calculates hash only by looking at filename and filesize
    """

    _type = 'file'

    def _get_hash(self) -> str:
        return get_file_hash(self._value)

    def serialize(self, cache: Path):
        if not self.value.exists():
            raise FileNotFoundError(f'Input file does not exist')
        super().serialize(
            cache,
            # Store the file hash along with the path to be able to verify later if file has not changed
            dict(
                path=str(self.value),
                hash=self._get_hash()
            )
        )

    def deserialize(self, cache: Path):
        super().deserialize(cache)
        # Check if stored hash still matches the file or is empty
        stored_hash = self._value['hash']
        self._value = Path(self._value['path'])
        if stored_hash == '' or stored_hash != self._get_hash():
            self._value = None


class FileOutput(TaskOutput):
    """
    An output representing a file based process output
    Calculates hash only by looking at filename and filesize
    """

    _type = 'file'

    def _get_hash(self) -> str:
        return get_file_hash(self._value)

    def serialize(self, cache: Path):
        if not self.value.exists():
            raise FileNotFoundError(f'Output file does not exist')
        super().serialize(
            cache,
            # Store the file hash along with the path to be able to verify later if file has not changed
            dict(
                path=str(self.value),
                hash=self._get_hash()
            )
        )

    def deserialize(self, cache: Path):
        super().deserialize(cache)
        # Check if stored hash still matches the file or is empty
        stored_hash = self._value['hash']
        self._value = Path(self._value['path'])
        if stored_hash == '' or stored_hash != self._get_hash():
            self._value = None


class FileInputChecksum(FileInput):
    """
    An input representing a file based process input
    Calculates a hash based on the file checksum and not only
    from file name and file size.
    """

    def _get_hash(self) -> str:
        return get_file_hash_checksum(self._value)


class FileOutputChecksum(FileOutput):
    """
    An output representing a file based process output
    Calculates a hash based on the file checksum and not only
    from file name and file size.
    """

    def _get_hash(self) -> str:
        return get_file_hash_checksum(self._value)


class FolderInput(TaskInput):
    """
    An input representing a collection of files as input
    Calculates hash only by looking at filenames and filesize
    of all files within folder
    """

    _type = 'folder'

    def _get_hash(self) -> str:
        return get_folder_hash(self._value)

    def serialize(self, cache: Path):
        if not self.value.exists():
            raise FileNotFoundError(f'Input path does not exist')
        super().serialize(
            cache,
            # Store the folder hash along with the path to be able to verify later if folder content has not changed
            dict(
                path=str(self.value),
                hash=self._get_hash()
            )
        )

    def deserialize(self, cache: Path):
        super().deserialize(cache)
        # Check if stored hash still matches the folder or is empty
        stored_hash = self._value['hash']
        self._value = Path(self._value['path'])
        if stored_hash == '' or stored_hash != self._get_hash():
            self._value = None


class FolderOutput(TaskOutput):
    """
    An output representing a collection of files
    Calculates hash only by looking at filenames and filesize
    of all files within folder
    """

    _type = 'folder'

    def _get_hash(self) -> str:
        return get_folder_hash(self._value)

    def serialize(self, cache: Path):
        if not self.value.exists():
            raise FileNotFoundError(f'Output path does not exist')
        super().serialize(
            cache,
            # Store the folder hash along with the path to be able to verify later if folder content has not changed
            dict(
                path=str(self.value),
                hash=self._get_hash()
            )
        )

    def deserialize(self, cache: Path):
        super().deserialize(cache)
        # Check if stored hash still matches the folder or is empty
        stored_hash = self._value['hash']
        self._value = Path(self._value['path'])
        if stored_hash == '' or stored_hash != self._get_hash():
            self._value = None


class FolderInputChecksum(FolderInput):
    """
    A class representing a collection of files as input
    Calculates a checksum over all files within the directory
    (Which might be slower for large or many files)
    """

    def _get_hash(self) -> str:
        return get_folder_hash_checksum(self._value)


class FolderOutputChecksum(FolderOutput):
    """
    A class representing the output of a collection of files
    Calculates a checksum over all files within the directory
    (Which might be slower for large or many files)
    """

    def _get_hash(self) -> str:
        return get_folder_hash_checksum(self._value)
