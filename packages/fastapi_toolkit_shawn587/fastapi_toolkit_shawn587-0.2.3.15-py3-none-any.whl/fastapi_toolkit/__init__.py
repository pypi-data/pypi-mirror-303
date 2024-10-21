from typing import Callable, Generator, Any, Annotated, Optional, Union, Coroutine, TypeVar

from sqlalchemy.orm import Session
from typing_extensions import Doc


def computed_field(db_func: Optional[Callable[..., Generator[Session, Any, None]]] = None):
    def decorator(func, *args, **kw):
        from pydantic import computed_field

        if db_func is not None:
            @computed_field(*args, **kw)
            def wrapper(*args_, **kw_) -> func.__annotations__.get('return'):
                return func(*args_, **kw_, db=next(db_func()))
        else:
            @computed_field(*args, **kw)
            def wrapper(*args_, **kw_) -> func.__annotations__.get('return'):
                return func(*args_, **kw_)
        return wrapper

    return decorator


T = TypeVar("T")


def Depends(  # noqa: N802
        dependency: Annotated[
            Optional[
                Union[
                    Callable[..., Coroutine[Any, Any, T]],
                    Callable[..., Generator[T, Any, Any]],
                    Callable[..., T],
                ]
            ],
            Doc(
                """
                A "dependable" callable (like a function).

                Don't call it directly, FastAPI will call it for you, just pass the object
                directly.
                """
            ),
        ] = None,
        *,
        use_cache: Annotated[
            bool,
            Doc(
                """
                By default, after a dependency is called the first time in a request, if
                the dependency is declared again for the rest of the request (for example
                if the dependency is needed by several dependencies), the value will be
                re-used for the rest of the request.

                Set `use_cache` to `False` to disable this behavior and ensure the
                dependency is called again (if declared more than once) in the same request.
                """
            ),
        ] = True,
) -> T:
    from fastapi import Depends
    return Depends(dependency, use_cache=use_cache)
