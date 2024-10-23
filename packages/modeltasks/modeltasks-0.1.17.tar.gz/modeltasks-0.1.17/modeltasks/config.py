import json
from configparser import (
    ConfigParser,
    ParsingError,
    DuplicateOptionError,
    DuplicateSectionError
)
from time import sleep
from dotenv import dotenv_values
from typing import Any, Dict, Union, List
from pathlib import Path
from modeltasks.util.hash import (
    get_hash,
    get_file_hash,
    get_file_hash_checksum,
    get_folder_hash,
    get_folder_hash_checksum
)
from modeltasks.log import logger
from modeltasks.util.task import TaskVariable


# Global settings dictionary
SETTINGS: Dict = dict(
    allow_pickle=False
)


def convert_parameter(parameter: str) -> Union[str, int, float, Dict, List, Path]:
    """
    Tries to convert the parameter string into the most probably type.
    If this is not possible, the convert methods falls back to returning the string representation.
    """
    if not isinstance(parameter, str):
        return parameter
    try:
        parameter = parameter.strip()
        if parameter.lower() in ('true', 'y', 'yes'):
            return True
        if parameter.lower() in ('false', 'n', 'no'):
            return False
        if parameter.isdigit():
            return int(parameter)
        if parameter[0] == '-' and parameter[1:].isdigit():
            return int(parameter[1:])*-1
        if parameter.replace('.', '', 1).replace('-', '', 1).isdigit():
            try:
                return float(parameter)
            except ValueError:
                return parameter
        elif parameter.startswith('"') and parameter.endswith('"'):
            return str(parameter.replace('"', ''))
        elif parameter.startswith("'") and parameter.endswith("'"):
            return str(parameter.replace("'", ''))
        elif parameter.startswith('{') and parameter.endswith('}'):
            return json.loads(parameter)
        elif parameter.startswith('[') and parameter.endswith(']') and ',' in parameter:
            return json.loads(parameter)
        elif ',' in parameter:
            return [convert_parameter(p.strip()) for p in parameter.split(',')]
        elif '/' in parameter or '\\' in parameter:
            if Path(parameter).is_file() or Path(parameter).is_dir():
                return Path(parameter)
            if (Path.cwd() / parameter).exists():
                return Path.cwd() / parameter
            return parameter
    except:
        pass
    return parameter


def load_configuration_file(config_file: Path) -> Dict:
    """
    Loads configuration parameters from a provided file.
    This method supports:
    - INI style files
    - JSON files
    - ENV files
    """

    config = {}
    config_file = Path(config_file)

    if config_file.exists() and config_file.is_file():
        try:
            logger.debug(f'Reading configuration file "{config_file}"')
            # JSON files
            if config_file.suffix.lower() == '.json':
                with open(config_file) as json_file:
                    json_data = json.load(json_file)
                    if isinstance(json_data, dict):
                        config = {k: convert_parameter(v) for k, v in json_data.items() if isinstance(v, str)}
                    else:
                        config = json_data
            # INI files
            elif config_file.suffix.lower() in ('.ini', '.cfg'):
                parser = ConfigParser()
                parser.read(config_file)
                config = {f'{s}_{k.upper()}': convert_parameter(v) for s in parser.sections() for k, v in parser.items(s)}

            # ENV files
            elif config_file.suffix.lower() == '.env':
                config = {k: convert_parameter(v) for k, v in dict(dotenv_values(config_file)).items()}
            else:
                logger.warning(f'Configuration file "{config_file}" is of unsupported type')
        except (
                json.JSONDecodeError,
                ParsingError,
                DuplicateOptionError,
                DuplicateSectionError
        ) as e:
            logger.error(f'Configuration file "{config_file}" cannot be read ({e})')

    # Return a dictionary with keys, values and parameter source info
    return {k: {'source': config_file, 'value': v} for k, v in config.items()}


class TaskParameter(TaskVariable):
    """
    The template class for defining model task configuration variables.
    Use this class to implement configuration classes and not the TaskVariable class.
    If a parameter is for instance a password, it should be obfuscated.
    """

    _key: str = None
    _options: Union[str, List] = None
    _obfuscate: bool = False
    _untracked: bool = False

    def __init__(self, key: str, *args, options: Union[str, Dict] = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._key = key
        self._options = options

    @property
    def key(self):
        return self._key

    @property
    def obfuscate(self):
        return self._obfuscate

    @property
    def untracked(self):
        return self._untracked

    def configure_value(self, value: Any = None):
        """
        This is a template method that can be used to implement value setting or
        lookup in parameter sub-classes. Instead of instantiating the variable with a value,
        the variable can be configured by the implemented procedure.
        """
        if value and not self._value:
            self._value = value


class ConfigurationValue(TaskParameter):
    """
    A configuration value
    """

    def _get_hash(self) -> str:
        return get_hash(self._value)


class SecureConfigurationValue(ConfigurationValue):
    """
    A configuration value that should be obfuscated
    """

    _obfuscate = True


class StaticConfigurationValue(TaskParameter):
    """
    A configuration value which can change its value but produces a static hash
    dependent on the parameter key and not its value.
    Use this variable if the value change does not influence the outputs. An example
    could be credential parameters. They might change but do not have an impact on
    outputs of a task.
    """

    _untracked = True

    def _get_hash(self) -> str:
        return get_hash(self._key)


class ConfigurationFile(TaskParameter):
    """
    A file path parameter
    Calculates hash from filesize and name of file
    """

    @TaskParameter.value.setter
    def value(self, v: Any):
        self.configure_value(Path(v))

    def _get_hash(self) -> str:
        return get_file_hash(self._value)


class ConfigurationFileChecksum(TaskParameter):
    """
    A file path parameter
    Calculates hash from checksum of file content
    """

    @TaskParameter.value.setter
    def value(self, v: Any):
        self.configure_value(Path(v))

    def _get_hash(self) -> str:
        return get_file_hash_checksum(self._value)


class ConfigurationFolder(TaskParameter):
    """
    A folder path parameter
    Calculates hash from filesize and name of all contained files
    """

    @TaskParameter.value.setter
    def value(self, v: Any):
        self.configure_value(Path(v))

    def _get_hash(self) -> str:
        return get_folder_hash(self._value)


class ConfigurationFolderChecksum(TaskParameter):
    """
    A folder path parameter
    Calculates hash from checksums of all contained files
    """

    @TaskParameter.value.setter
    def value(self, v: Any):
        self.configure_value(Path(v))

    def _get_hash(self) -> str:
        return get_folder_hash_checksum(self._value)


class UserInput(TaskParameter):
    """
    A class representing the live input made by a user
    Calculates a checksum over the input and makes sure
    that checksums for the same user input stay the same
    """

    def _get_hash(self) -> str:
        return get_hash(self._value)

    def serialize(self, location):
        pass

    def configure_value(self, value: Any = None):
        logger.info(f'Asking for user input (Parameter: {self._key})')
        sleep(0.1)
        if not self._value:
            self._value = input(f'Enter value for parameter ({self._key}):  ' if not self._options else f'{self._options} ({self._key}): ').strip()


class SecureUserInput(UserInput):
    """
    A class representing the secure input made by a user,
    for instance passwords that should no show up in logs.
    Calculates a checksum over the input and makes sure
    that checksums for the same user input stay the same
    """

    _obfuscate = True


class UserSelection(TaskParameter):
    """
    A class representing the live selection made by a user.
    Calculates a checksum over the input and makes sure
    that checksums for the same user input stay the same
    """

    def _get_hash(self) -> str:
        return get_hash(self._value)

    def serialize(self, location):
        pass

    def configure_value(self, value: Any = None):
        logger.info(f'Asking for user selection (Parameter: {self._key})')
        sleep(0.1)
        if not self._value:
            print(f'Options for parameter ({self._key}):')
            for o in self._options:
                print(f'  - {o}')
            selected = input(f'Enter one of the above options for parameter ({self._key}): ').strip()
            if (value := convert_parameter(selected)) in self._options:
                self.value = value
            else:
                logger.error(f'Selected wrong option "{selected}" for parameter ({self._key})')
