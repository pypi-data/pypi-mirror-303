from ollama import Client as _OllamaClient # type: ignore
from fundar_llms.api.interface import PlainPromptInterface, Base64
from fundar_llms.cuda import get_available_vram
from typing import Optional, Any

OLLAMA_DEFAULT_OPTIONS = dict(
    mirostat=0,           # int
    mirostat_eta=0.1,     # float
    mirostat_tau=5.0,     # float
    num_ctx=2048,         # int
    repeat_last_n=64,     # int
    repeat_penalty=1.1,   # float
    temperature=0.8,      # float
    seed=0,               # int
    stop=[],              # string
    tfs_z=1,              # float
    num_predict=128,      # int
    top_k=40,             # int
    top_p=0.9,            # float
    min_p=0.0             # float
)

class OllamaClient(PlainPromptInterface, _OllamaClient):
    def list_models(self, max_vram = None): # default max vram: (3.2 * 1.074E9)
        if max_vram is None:
            max_vram, _ = get_available_vram()
        models = self.list()
        models = models['models']
        models = [
            model['name']
            for model in models
            if model['size'] <= max_vram
        ]

        return models
    
    def generate(
            self,
            model: str,
            prompt: str,
            raw: Optional[bool] = None,
            image: Optional[Base64] = None,
            suffix: Optional[str] = None,
            format: Optional[str] = None,
            system: Optional[str] = None,
            context: Optional[Any] = None,
            stream: Optional[bool] = None,
            num_ctx: Optional[int] = None,
            num_predict: Optional[int] = None,
            temperature: Optional[float] = None,
            top_k: Optional[int] = None,
            top_p: Optional[float] = None,
            *args,
            **kwargs
    ) -> Any:
        options = dict(
            temperature = temperature,
            top_k = top_k,
            top_p = top_p,
            num_ctx = num_ctx,
            num_predict = num_predict
        )

        if not stream:
            stream = False

        options = OLLAMA_DEFAULT_OPTIONS | options # type: ignore

        return _OllamaClient.generate( # type: ignore
            self,
            model=model,
            prompt=prompt,
            system=system,
            # template=template,
            context=context,
            stream=stream,
            raw=raw,
            format=format,
            # images=images,
            options=options,
            **kwargs
        )