from typing import TypeVar, Sequence, Callable, Any, ParamSpec, TypedDict, Unpack
from collections.abc import Iterable
from functools import wraps
import inspect

P = ParamSpec('P')
T = TypeVar('T')

def flatten(nested_list: Sequence[Sequence[T]], max_level=5) -> Sequence[T]:
    return _flatten(nested_list, max_level)

def _flatten(nested_list: Sequence[T | Sequence[T]], current_level) -> Sequence[T]:
    if current_level == 0:
        return nested_list # type: ignore
    else:
        return _flatten([item # type: ignore
                         for sublist in nested_list 
                         for item in sublist # type: ignore
                         if isinstance(item, Iterable)]
                         , current_level-1)
    
def split_list_into_chunks(lst: list[T], chunk_size: int):
    return [lst[i:j] for i, j in 
            ((i, i + chunk_size) 
                for i in range(0, len(lst), chunk_size))]


def allow_opaque_constructor(**objects):
    def wrapper(f: Callable[P, T]) -> Callable[P, T]:
        sig = inspect.signature(f)

        assert all(x in sig.parameters.keys() for x in objects)

        @wraps(f)
        def _(*args, **kwargs) -> T:
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            bound_args = bound_args.arguments # type: ignore
            
            for k,v in bound_args.items(): # type: ignore
                if k not in objects:
                    continue
                if not isinstance(v, dict):
                    continue
                bound_args[k] = objects[k](**v) # type: ignore
            return f(**bound_args) # type: ignore
        return _
    return wrapper