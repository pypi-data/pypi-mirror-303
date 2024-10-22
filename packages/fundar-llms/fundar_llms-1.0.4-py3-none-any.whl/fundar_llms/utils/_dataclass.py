from abc import ABC as AbstractBaseClass
from dataclasses import asdict
from typing import Any

class DataclassDictUtilsMixin(AbstractBaseClass):
    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        return cls(**data)
    
    def to_dict(self, compact=False) -> dict[str, Any]:
        data = asdict(self) # type: ignore
        
        if compact :
            data = {k:v for k,v in data.items() if v}
        
        return data