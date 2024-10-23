from typing import Protocol, Optional, Any
from dataclasses import dataclass
from fundar_llms import Base64, Context
from fundar_llms.utils import DataclassDictUtilsMixin

response_dataclass_options = dict(
    init            = True,
    repr            = True,
    eq              = True,
    order           = False,
    unsafe_hash     = True,
    frozen          = True,
    match_args      = False,
    kw_only         = True,
    slots           = True,
    weakref_slot    = False,
)

@dataclass(**response_dataclass_options)
class BaseResponse(DataclassDictUtilsMixin):
    model: str
    prompt: str
    system: str
    response: str
    total_duration: int
    load_duration: Optional[int] = None
    done: Optional[bool] = None
    done_reason: Optional[str] = None
    context: Optional[Context] = None
    num_ctx: Optional[int] = None
    num_predict: Optional[int] = None
    temperature: Optional[float] = None
    top_k: Optional[float] = None
    top_p: Optional[float] = None
    extra: Optional[Any] = None


class PlainPromptInterface(Protocol):
    def generate(
            self,
            model: str,
            prompt: str,
            raw: Optional[bool] = None,
            image: Optional[Base64] = None,
            suffix: Optional[str] = None,
            format: Optional[str] = None,
            system: Optional[str] = None,
            context: Optional[Context] = None,
            stream: Optional[bool] = None,
            num_ctx: Optional[int] = None,
            num_predict: Optional[int] = None,
            temperature: Optional[float] = None,
            top_k: Optional[int] = None,
            top_p: Optional[float] = None,
            *args,
            **kwargs
    ) -> Any: ...


