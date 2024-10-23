from fundar_llms.utils.models import modelname
from dataclasses import dataclass
from typing import Optional

tokenizer_model_dataclass_options = dict(
    init            = True,
    repr            = True,
    eq              = True,
    order           = False,
    unsafe_hash     = True,
    frozen          = True,
    match_args      = True,
    kw_only         = False,
    slots           = True,
    weakref_slot    = False,
)

auto_tokenizer_ = None

@dataclass(**tokenizer_model_dataclass_options)
class TokenizerModel:
    name: str
    needs_auth: bool = True

    def __str__(self):
        return self.name

    def auto_tokenizer_from_pretrained(self):
        global auto_tokenizer_
        if not auto_tokenizer_:
            from transformers import AutoTokenizer # type: ignore
            auto_tokenizer_ = AutoTokenizer
        
        if self.needs_auth:
            from dotenv import find_dotenv, dotenv_values
            from huggingface_hub import login # type: ignore
            login(dotenv_values(find_dotenv())['HUGGINGFACE_API_KEY'])
        
        return auto_tokenizer_.from_pretrained(self.name)

            
# Acá silencio al typechecker porque no detecta el __init__ generado por la dataclass.
DEFAULT_TOKENIZER_MAP = {
    'phi3.5': \
        TokenizerModel('microsoft/Phi-3.5-mini-instruct', needs_auth=False), # type: ignore
    'phi3': \
        TokenizerModel('microsoft/Phi-3-mini-128k-instruct', needs_auth=False), # type: ignore
    'llama3.1': \
        TokenizerModel('meta-llama/Llama-3.1-8B-Instruct', needs_auth=True), # type: ignore
    'llama3.2': \
        TokenizerModel('meta-llama/Llama-3.2-3B-Instruct', needs_auth=True), # type: ignore
}

def get_tokenizer(model_name: str, 
                  tokenizer_map: Optional[dict[str, TokenizerModel]] = None, 
                  default: Optional[TokenizerModel] = None) -> TokenizerModel:
    if not tokenizer_map:
        global DEFAULT_TOKENIZER_MAP
        tokenizer_map = DEFAULT_TOKENIZER_MAP
    
    if not default:
        default = tokenizer_map['phi3.5']
    
    return tokenizer_map.get(modelname(model_name), default)

