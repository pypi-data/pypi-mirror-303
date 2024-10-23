from numpy import argsort
from typing import Optional
from collections.abc import Iterable

def subdict(d, keys):
    return {k: d[k] for k in keys}

_reranker = None

def upsert_reranker_model(
        model_name='cross-encoder/ms-marco-MiniLM-L-6-v2', 
        device='cuda', 
        **kwargs
    ):

    global _reranker
    if _reranker is None:
        from sentence_transformers import CrossEncoder
        _reranker = CrossEncoder(model_name=model_name, **kwargs)
    else:
        if (_reranker.model.name_or_path != model_name) or (_reranker.model.device.type != device):
            crossencoder_t = type(_reranker)
            del _reranker
            _reranker = crossencoder_t(model_name=model_name, **kwargs)
    return _reranker


_ALL_RERANK_ELEMENTS = ('elements', 'query', 'scores')
def _process_rerank(cross_encoder, universe: Iterable[str], query: str, include: Iterable[str]):
    assert all(x in _ALL_RERANK_ELEMENTS for x in include)

    pairs = [[query, x] for x in universe]
    scores_ = cross_encoder.predict(pairs)
    indices = argsort(scores_)[::-1]

    for i in indices:
        result = dict(
            elements = universe[i],
            query = query,
            scores = scores_[i]
        )

        yield tuple(subdict(result, include).values())

_INCLUDE_MAP = dict(
    all = _ALL_RERANK_ELEMENTS,
    score = ('scores', ),
    queries = ('query', ),
    element = ('elements', ),
)

def rerank(
        universe: Iterable[str], 
        query: str, 
        cross_encoder = None, 
        include: Optional[Iterable[str]] = None,
        *args,
        **kwargs,
):
    if not cross_encoder:
        cross_encoder = upsert_reranker_model()

    if include is None:
        include = ('all', )
    
    _include: tuple = tuple(_INCLUDE_MAP[x] for x in include)
    include = tuple(set(y for x in _include for y in x))

    return list(_process_rerank(
        cross_encoder=cross_encoder,
        query=query,
        universe=universe,
        include=include
    ))