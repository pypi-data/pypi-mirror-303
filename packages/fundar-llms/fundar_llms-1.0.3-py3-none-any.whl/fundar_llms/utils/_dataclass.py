from abc import ABC as AbstractBaseClass
from dataclasses import asdict

class DataclassDictUtilsMixin(AbstractBaseClass):
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    def to_dict(self, compact=False):
        data = asdict(self)
        
        if compact :
            data = {k:v for k,v in data.items() if v}
        
        return data