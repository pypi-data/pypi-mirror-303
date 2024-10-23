import timeit
import logging
from functools import wraps
from typing import Any, Dict
from threading import Condition, Lock


class TaskVariable:
    """
    The base class for the implementation of any task parameter,
    being it inputs, outputs configs, etc.
    It encapsulates a value property and maps specific outer variable functions
    internally to the value.
    """

    _value: Any = None
    _is_set: bool = False
    _wrapper_cache: Dict = None
    _protected = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v: Any):
        if v is not None:
            if self._value is None:
                self._value = v
                self._is_set = True
            else:
                raise AttributeError(f'Cannot set value twice (Value="{self.value}", New value="{v}"')

    @property
    def is_set(self):
        return self._is_set

    @property
    def hash(self) -> str:
        return self._get_hash()

    def __init__(self, value: Any = None):
        # Add some default protected attributes
        self._add_protected([
                '__repr__',
                '__dict__',
                '__class__',
                '__name__',
                '__annotations__',
                '__str__',
                '_value',
                'value'
                # '_wrap_value_method',
                # '_wrapper_cache',
                # '_id',
                # '_type',
                # '_task',
                # '_key',
                # '_is_set',
                # '_options',
                # '_get_hash',
                # '_cacheable',
                # '_get_other_value',
                # 'id',
                # 'identifier',
                # 'task'
                # 'key',
                # 'is_set',
                # 'options',
                # 'hash',
                # 'cacheable',
                # 'configure_value',
                # 'serialize',
                # 'deserialize'
                # 'is_cached'
            ] +
            list(super().__getattribute__('__dict__').keys()) +
            list(super().__getattribute__('__class__').__dict__.keys())
        )

        if value is not None:
            self.value = value
        """
        The wrapper cache needs to be specific for each variable and cannot be a 
        shared dictionary because of the wrapped method scope
        """
        self._wrapper_cache = {}

    def _add_protected(self, attributes: [str]):
        """
        Because we wrap a value object inside of this class we need to decide which attributes
        should be resolved internally and which ones should me mapped to the value object.
        To protect certain class attributes, you can add them with this method.
        """
        self._protected = list(set(
            self._protected +
            attributes
        ))

    def _get_hash(self) -> str:
        """Template method to return hash"""
        return self._value.__hash__

    def _wrap_value_method(self, attribute, method):
        try:
            return self._wrapper_cache[attribute]
        except KeyError:
            @wraps(method)
            def wrapper(*args, **kwargs):
                return method(*args, **kwargs)
            self._wrapper_cache.update({
                attribute: wrapper
            })
            return wrapper

    @staticmethod
    def _get_other_value(other):
        if hasattr(other, '_get_other_value'):
            try:
                return other.value
            except AttributeError:
                pass
        return other

    def __getattribute__(self, attribute):
        if attribute not in [
            '__dict__',
            '_protected',
            '_add_protected'
        ] + super().__getattribute__('_protected'):
            try:
                # Get the attribute from the encapsulated value
                encapsulated_value = self._value.__getattribute__(attribute)
            except AttributeError:
                # Encapsulated value does not have the attribute, so it seems the attribute refers to the TaskVariable
                return super().__getattribute__(attribute)
            if callable(encapsulated_value):
                # Wrap the attribute if it is a method
                return self._wrap_value_method(attribute, encapsulated_value)
            else:
                # Otherwise just return it
                return encapsulated_value
        else:
            # Get the attribute straight from the TaskVariable
            return super().__getattribute__(attribute)

    def __repr__(self) -> Any:
        return f'<{self.__class__.__name__}={self._value}>'

    def __str__(self) -> Any:
        return self._value.__str__()

    # Comparison operators

    def __eq__(self, other) -> Any:
        return self._value.__eq__(self._get_other_value(other))

    def __ne__(self, other) -> Any:
        return self._value.__ne__(self._get_other_value(other))

    def __gt__(self, other):
        return self._value.__gt__(self._get_other_value(other))

    def __ge__(self, other):
        return self._value.__ge__(self._get_other_value(other))

    def __lt__(self, other):
        return self._value.__lt__(self._get_other_value(other))

    def __le__(self, other):
        return self._value.__le__(self._get_other_value(other))

    def __bool__(self):
        return bool(self._value)

    def __hash__(self):
        return self._value.__hash__()

    def __sizeof__(self):
        return self._value.__sizeof__()

    def __nonzero__(self):
        return self._value.__nonzero__()

    # Numeric types

    def __add__(self, other):
        return self._value.__add__(self._get_other_value(other))

    def __radd__(self, other):
        return self._value.__radd__(self._get_other_value(other))

    def __iadd__(self, other):
        return self._value.__iadd__(self._get_other_value(other))

    def __sub__(self, other):
        return self._value.__sub__(self._get_other_value(other))

    def __rsub__(self, other):
        return self._value.__rsub__(self._get_other_value(other))

    def __isub__(self, other):
        return self._value.__isub__(self._get_other_value(other))

    def __mul__(self, other):
        return self._value.__mul__(self._get_other_value(other))

    def __rmul__(self, other):
        return self._value.__rmul__(self._get_other_value(other))

    def __imul__(self, other):
        return self._value.__imul__(self._get_other_value(other))

    def __truediv__(self, other):
        return self._value.__truediv__(self._get_other_value(other))

    def __rtruediv__(self, other):
        return self._value.__rtruediv__(self._get_other_value(other))

    def __itruediv__(self, other):
        return self._value.__itruediv__(self._get_other_value(other))

    def __floordiv__(self, other):
        return self._value.__floordiv__(self._get_other_value(other))

    def __rfloordiv__(self, other):
        return self._value.__rfloordiv__(self._get_other_value(other))

    def __ifloordiv__(self, other):
        return self._value.__ifloordiv__(self._get_other_value(other))

    def __mod__(self, other):
        return self._value.__mod__(self._get_other_value(other))

    def __rmod__(self, other):
        return self._value.__rmod__(self._get_other_value(other))

    def __imod__(self, other):
        return self._value.__imod__(self._get_other_value(other))

    def __divmod__(self, other):
        return self._value.__divmod__(self._get_other_value(other))

    def __rdivmod__(self, other):
        return self._value.__rdivmod__(self._get_other_value(other))

    def __pow__(self, other):
        return self._value.__pow__(self._get_other_value(other))

    def __rpow__(self, other):
        return self._value.__rpow__(self._get_other_value(other))

    def __ipow__(self, other):
        return self._value.__ipow__(self._get_other_value(other))

    def __lshift__(self, other):
        return self._value.__lshift__(self._get_other_value(other))

    def __rlshift__(self, other):
        return self._value.__rlshift__(self._get_other_value(other))

    def __ilshift__(self, other):
        return self._value.__ilshift__(self._get_other_value(other))

    def __rshift__(self, other):
        return self._value.__rshift__(self._get_other_value(other))

    def __rrshift__(self, other):
        return self._value.__rrshift__(self._get_other_value(other))

    def __irshift__(self, other):
        return self._value.__irshift__(self._get_other_value(other))

    def __and__(self, other):
        return self._value.__and__(self._get_other_value(other))

    def __rand__(self, other):
        return self._value.__rand__(self._get_other_value(other))

    def __iand__(self, other):
        return self._value.__iand__(self._get_other_value(other))

    def __xor__(self, other):
        return self._value.__xor__(self._get_other_value(other))

    def __rxor__(self, other):
        return self._value.__rxor__(self._get_other_value(other))

    def __ixor__(self, other):
        return self._value.__ixor__(self._get_other_value(other))

    def __abs__(self):
        return self._value.__abs__()

    def __invert__(self):
        return self._value.__invert__()

    def __pos__(self):
        return self._value.__pos__()

    def __oct__(self):
        return self._value.__oct__()

    def __hex__(self):
        return self._value.__hex__()

    def __int__(self):
        return self._value.__int__()

    def __float__(self):
        return self._value.__float__()

    def __complex__(self):
        return self._value.__complex__()

    def __round__(self, n):
        return self._value.__round__(n)

    def __trunc__(self):
        return self._value.__trunc__()

    def __floor__(self):
        return self._value.__floor__()

    def __ceil__(self):
        return self._value.__ceil__()

    def __neg__(self):
        return self._value.__neg__()

    def __index__(self):
        return self._value.__index__()

    def __contains__(self, value):
        return self._value.__contains__(self._get_other_value(value))

    def __copy__(self):
        return self._value.__copy__()

    def __deepcopy__(self):
        return self._value.__deepcopy__()

    def __len__(self):
        return self._value.__len__()

    def __getitem__(self, other):
        return self._value.__getitem__(self._get_other_value(other))

    def __setitem__(self, key, value):
        return self._value.__setitem__(key, self._get_other_value(value))

    def __delitem__(self, key):
        return self._value.__delitem__(key)

    def __missing__(self, key):
        return self._value.__missing__(key)

    def __iter__(self):
        return self._value.__iter__()

    def __reversed__(self):
        return self._value.__reversed__()


class ConditionalSemaphore:
    def __init__(self, max_slots: int, blocking: bool = True):
        self._count = 0
        self._max_slots = max_slots
        self._blocking = blocking
        self._lock = Condition(lock=Lock())

    @property
    def count(self):
        with self._lock:
            return self._count

    def acquire(self):
        with self._lock:
            while self._count >= self._max_slots:
                if self._blocking:
                    self._lock.wait()
            self._count += 1

    def release(self):
        with self._lock:
            self._count -= 1
            self._lock.notify()

    def is_reset(self):
        with self._lock:
            return self._count == 0


class ExecutionTimer:
    def __init__(self, name=None, logger: logging.Logger = None, executor: str = None, failed: str = None):
        self.name = name
        self.logger = logger
        self.executor = executor
        self.failed = failed

    def log(self, message: str):
        if self.logger:
            self.logger.info(message)
        else:
            logging.info(message)

    def __enter__(self):
        self.start = timeit.default_timer()
        self.log(f'Task "{self.name}": Starting task{" (" + str(self.executor) + ") " if self.executor is not None else ""}...')

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = (timeit.default_timer() - self.start)
        if not self.failed:
            self.log(f'Task "{self.name}": Completed in {round(self.took, 6)} seconds')
