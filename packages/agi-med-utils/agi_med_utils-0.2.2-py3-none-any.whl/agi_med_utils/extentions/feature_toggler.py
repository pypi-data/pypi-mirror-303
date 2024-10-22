from typing import TypeVar, Type, Any, Callable, get_origin, get_args
from functools import wraps
from types import UnionType, NoneType

T = TypeVar("T", bound=Type)


class FeatureToggler:
    """
    Class for disable methods.
    Usage:
        ```
        @FeatureToggler(enable=False)
        class PostgresManager:
        def __init__(self):
            self._postgres = create_engine('postgresql+psycopg2://user:password@127.0.0.1:5432/db')

        def test(self) -> int:
            with self._postgres.connect() as conn:
                conn.execute(text("SELECT 1;"))
            return 124  # Output: 0

        @FeatureToggler.ignore # Method ignored override
        def another_test(self) -> int:
            with self._postgres.connect() as conn:
                conn.execute(text('SELECT 2;'))
            return 777  # Output: 777
        ```
    Required: Annotation in functions!

    TODO Plans:
        1. add correct handling of cases when the method returns an instance of itself. Now will be None

    """

    __slots__ = ("_enable",)

    def __init__(self, enable: bool = True) -> None:
        self._enable: bool = enable

    def _default_value_by_type(self, return_type: Type) -> Any:
        """Return value by annotation."""
        returning_tuple_types: tuple = (return_type, get_origin(return_type))
        if int in returning_tuple_types:
            return 0
        if str in returning_tuple_types:
            return ""
        if list in returning_tuple_types:
            return []
        if dict in returning_tuple_types:
            return {}
        if bool in returning_tuple_types:
            return False
        if set in returning_tuple_types:
            return set()
        if frozenset in returning_tuple_types:
            return frozenset([])
        if bytes in returning_tuple_types:
            return bytes([])
        if UnionType in returning_tuple_types:
            return self._process_union_type(return_type)
        return None

    def _process_union_type(self, return_type: Type) -> Any:
        args: tuple[Any, ...] = get_args(return_type)
        if NoneType in args:
            return None
        for arg in args:
            default_value = self._default_value_by_type(arg)
            if default_value is not None:
                return default_value
        return None

    def disable_method(self, method: Callable) -> Callable:
        @wraps(method)
        def wrapper(*args, **kwargs) -> Any:
            return_type: Type | None = method.__annotations__.get("return", None)  # type: ignore
            return self._default_value_by_type(return_type)

        return wrapper

    def disable_property(self, prop: property) -> property:
        @property
        @wraps(prop.fget)
        def wrapper(*_) -> Any:
            return_type: Type | None = prop.fget.__annotations__.get("return", None)  # type: ignore
            return self._default_value_by_type(return_type)

        return wrapper

    def enable_method_by_dependency(self, enable: bool = True) -> Callable:
        def wrapper(func):
            if enable is False:
                return self.disable_method(func)
            return func

        return wrapper

    def __call__(self, cls: T) -> T:
        if not self._enable:
            for attr_name in dir(cls):
                attr = getattr(cls, attr_name)
                if attr_name.startswith("__") and attr_name.endswith("__"):
                    if not getattr(attr, "_force_override", False):
                        continue
                if callable(attr):
                    if getattr(attr, "_ignore", False):
                        continue
                    setattr(cls, attr_name, self.disable_method(attr))
                elif isinstance(attr, property):
                    if getattr(attr.fget, "_ignore", False):
                        continue
                    setattr(cls, attr_name, self.disable_property(attr))
        return cls

    @staticmethod
    def ignore(method: Callable) -> Any:
        """
        Wrapper for mark ignored methods
        """
        method._ignore = True
        return method

    @staticmethod
    def force_override(method: Callable) -> Any:
        """
        Wrapper for include dunder methods to override (default excludes)
        """
        method._force_override = True
        return method
