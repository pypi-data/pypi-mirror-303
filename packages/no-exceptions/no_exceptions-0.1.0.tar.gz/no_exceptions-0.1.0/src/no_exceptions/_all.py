from typing import Callable, Generic, Optional, Tuple, Type, TypeVar, Union, cast

RetType = TypeVar("RetType")
OkType = TypeVar("OkType")

NoArgsClosure = Callable[[], RetType]
"""A type alias for a function that takes no arguments and returns a value of type `RetType`."""


class Result(Generic[OkType]):
    """Represents a result of an operation, containing either a success value or an error."""

    def __init__(self, val: Union[OkType, Exception], *, is_ok: bool) -> None:
        """
        Initialize a new `Result` object.

        Args:
            val (Union[OkType, Exception]): The value or exception to be stored in the result. If the result is
                successful, this should be the success value (`OkType`). If the result contains an error, this should be
                an `Exception` object.
            is_ok (bool): A flag indicating whether the result represents success (`True`) or an error (`False`).
        """
        self._inner = val
        self._is_ok = is_ok

    @property
    def is_ok(self) -> bool:
        """
        Check if the result is successful.

        Returns:
            bool: `True` if the result is successful (i.e., not an `Exception`), `False` otherwise.

        Example:
            >>> result = Result(42, is_ok=True)
            >>> result.is_ok
            True
        """
        return self._is_ok

    @property
    def is_err(self) -> bool:
        """
        Check if the result contains an error.

        Returns:
            bool: `True` if the result contains an error (i.e., an `Exception`), `False` otherwise.

        Example:
            >>> result = Result(ZeroDivisionError(), is_ok=False)
            >>> result.is_err
            True
        """
        return not self.is_ok

    def unpack(self) -> Tuple[bool, Optional[OkType]]:
        """
        Unpack the result into a tuple indicating success and the associated value or `None`.

        Returns:
            Optional[OkType]: A tuple where the first element is a `bool` indicating success (`True`) or failure
                (`False`), and the second element is the success value or `None`.

        Example:
            >>> result = Result(42, is_ok=True)
            >>> result.unpack()
            (True, 42)
            >>> error_result = Result(ZeroDivisionError(), is_ok=False)
            >>> error_result.unpack()
            (False, None)
        """
        if self.is_ok:
            return True, cast(OkType, self._inner)
        return False, None

    def unwrap(self) -> OkType:
        """
        Unwrap the success value from the result or raise a `ValueError` if the result contains an error.

        Raises:
            ValueError: If the result contains an error (`Exception`).

        Returns:
            OkType: The success value if the result is successful.

        Example:
            >>> result = Result(42, is_ok=True)
            >>> result.unwrap()
            42
            >>> error_result = Result(ZeroDivisionError(), is_ok=False)
            >>> error_result.unwrap()
            Traceback (most recent call last):
            ...
            ValueError: Tried to unwrap an erroneous result: Result(ZeroDivisionError())!
        """
        if self.is_err:
            raise ValueError(f"Tried to unwrap an erroneous result: {repr(self)}!")
        return cast(OkType, self._inner)

    def unwrap_or(self, default: OkType) -> OkType:
        """
        Unwrap the success value, or return a default value if the result contains an error.

        Args:
            default (OkType): The default value to return if the result contains an error.

        Returns:
            OkType: The success value if the result is successful, `default` value otherwise.

        Example:
            >>> result = Result(42, is_ok=True)
            >>> result.unwrap_or(0)
            42
            >>> error_result = Result(ZeroDivisionError(), is_ok=False)
            >>> error_result.unwrap_or(0)
            0
        """
        if self.is_ok:
            return cast(OkType, self._inner)
        return default

    def __str__(self) -> str:
        return f"Fallible operation result: {str(self._inner)}"

    def __repr__(self) -> str:
        return f"Result({repr(self._inner)})"


def try_expecting(closure: NoArgsClosure[RetType], expected_error: Type[Exception]) -> Result[RetType]:
    """
    Execute a function and return a `Result` object, capturing any expected errors.

    This function attempts to execute the provided `closure` (typically a `lambda` with no arguments). If the function
    completes successfully, the result is encapsulated in a `Result` object with a successful status. If the specified
    `expected_error` is raised during execution, it captures the error in the `Result` as a failure.

    Args:
        closure (NoArgsClosure[RetType]): A function that takes no arguments and returns a value of type `RetType`.
        expected_error (Type[Exception]): The exception type that should be caught and treated as an error.

    Returns:
        Result[RetType, Exception]: A `Result` object containing either the successful return value from `closure` or
            the caught exception.

    Example:
        >>> try_expecting(lambda: 55 / 0, ZeroDivisionError)
        Result(ZeroDivisionError('division by zero'))
        >>> try_expecting(lambda: 55 / 0, ZeroDivisionError).unwrap_or(1)
        1
        >>> try_expecting(lambda: 4 / 2, ZeroDivisionError)
        Result(2.0)
        >>> ok, res = try_expecting(lambda: 4 / 2, ZeroDivisionError).unpack()
        >>> ok, res
        (True, 2.0)
    """
    try:
        return Result(closure(), is_ok=True)
    except expected_error as error:
        return Result(error, is_ok=False)
