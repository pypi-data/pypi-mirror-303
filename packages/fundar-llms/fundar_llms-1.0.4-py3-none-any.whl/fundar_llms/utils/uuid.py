import random
from typing import Any, Optional, Iterable, Callable, ParamSpec, TypeVar
import uuid
import inspect
from types import GeneratorType
from functools import wraps
import collections
from itertools import islice

P = ParamSpec('P')
T = TypeVar('T')

def consume(iterator: Iterable[Any], n: Optional[int] = None) -> None:
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    if n is None:
        collections.deque(iterator, maxlen=0)
    else:
        next(islice(iterator, n, n), None)

def pass_generator_as_copy(*xs: Iterable[str]):
    def wrapper(f: Callable[P, T]) -> Callable[P, T]:
        sig = inspect.signature(f)

        assert all(x in sig.parameters.keys() for x in xs)

        @wraps(f)
        def _(*args, **kwargs) -> T:
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            bound_args = bound_args.arguments # type: ignore
            
            for k,v in bound_args.items(): # type: ignore
                if not k in xs:
                    continue
                if not isinstance(v, GeneratorType):
                    continue
                bound_args[k] = list(v) # type: ignore
            return f(**bound_args) # type: ignore
        return _
    return wrapper

class UuidGenerator:
    def __init__(self, seed: Optional[int] = None):
        self.seed = seed
        self._instantiate_random()

    def _instantiate_random(self):
        self.random = random.Random()

        if self.seed is not None:
            self.random.seed(self.seed)

        return self
    
    def reset(self):
        return self._instantiate_random()

    def _next(self):
        return uuid.UUID(int=self.random.getrandbits(128), version=4)

    def next(self, n: Optional[int] = None):
        if n is None:
            return self._next()
        else:
            return (self._next() for _ in range(n))
    
    def __iter__(self):
        while True:
            yield self.next()

    @pass_generator_as_copy('xs')
    def map(self, xs: Iterable[T], offset: Optional[int] = None) -> Iterable[uuid.UUID]: 
        if offset is not None:
            self.reset()

            if offset > 0:
                consume(self.next(offset))
        
        return map(lambda _: self.next(), xs)

    @pass_generator_as_copy('xs')
    def zipWith(self, xs: Iterable[T], offset: Optional[int] = None) -> Iterable[tuple[uuid.UUID, T]]:
        return zip(self.map(xs, offset=offset), xs)