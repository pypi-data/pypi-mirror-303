from tqdm.contrib.concurrent import process_map
from langchain.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from collections.abc import Iterable, Sized
from typing import Optional
import uuid
import random
import collections
from itertools import islice
from copy import copy
from types import GeneratorType
import inspect
from functools import wraps, reduce
from operator import or_ as union
from typing import TypeVar, Sequence, Callable
from pydantic import Field
import subprocess
import torch

T = TypeVar('T')

def flatten(nested_list: Sequence[Sequence[T]], max_level=5) -> Sequence[T]:
    return _flatten(nested_list, max_level)

def _flatten(nested_list: Sequence[T | Sequence[T]], current_level) -> Sequence[T]:
    if current_level == 0:
        return nested_list
    else:
        return _flatten([item 
                         for sublist in nested_list 
                         for item in sublist 
                         if isinstance(item, Iterable)]
                         , current_level-1)

def split_list_into_chunks(lst: list[T], chunk_size: int):
    return [lst[i:j] for i, j in 
            ((i, i + chunk_size) 
                for i in range(0, len(lst), chunk_size))]

def pass_generator_as_copy(*xs):
    def wrapper(f):
        sig = inspect.signature(f)

        assert all(x in sig.parameters.keys() for x in xs)

        @wraps(f)
        def _(*args, **kwargs):
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            bound_args = bound_args.arguments
            
            for k,v in bound_args.items():
                if not k in xs:
                    continue
                if not isinstance(v, GeneratorType):
                    continue
                bound_args[k] = list(v)
            return f(**bound_args)
        return _
    return wrapper

def allow_opaque_constructor(**objects):
    def wrapper(f):
        sig = inspect.signature(f)

        assert all(x in sig.parameters.keys() for x in objects)

        @wraps(f)
        def _(*args, **kwargs):
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            bound_args = bound_args.arguments
            
            for k,v in bound_args.items():
                if k not in objects:
                    continue
                if not isinstance(v, dict):
                    continue
                bound_args[k] = objects[k](**v)
            return f(**bound_args)
        return _
    return wrapper

def consume(iterator, n=None):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    if n is None:
        collections.deque(iterator, maxlen=0)
    else:
        next(islice(iterator, n, n), None)

_is_cuda_available_ = None
def is_cuda_available() -> bool:
    global _is_cuda_available_
    if _is_cuda_available_ is None:
        from torch.cuda import is_available as is_cuda_available_
        _is_cuda_available_ = is_cuda_available_
    return _is_cuda_available_()

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

DEFAULT_PDF_LOADER = PyPDFLoader

def load_document(filepath: str, loader = None, seed_id: Optional[int] = -1) -> list[Document]:
    # Un Document por página
    if not loader:
        loader = DEFAULT_PDF_LOADER
    
    assert hasattr(loader, 'load')
    
    result = loader(filepath).load()

    if seed_id != -1:
        uuid_generator = UuidGenerator(seed_id)
        for doc in result:
            doc.id = uuid_generator.next()
    
    return result
        

DEFAULT_RCT_SPLITTER = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", "(?<=\. )", " ", "", "-\n"],
        chunk_size=1000,
        chunk_overlap=0,
        add_start_index=True
)

@allow_opaque_constructor(splitter = RecursiveCharacterTextSplitter)
def split_document(xs, splitter = None, seed_id: Optional[int] = -1) -> list[Document]:
    if not splitter:
        splitter = DEFAULT_RCT_SPLITTER

    assert hasattr(splitter, 'split_documents')
    
    if isinstance(xs, Document):
        xs = [xs]
    
    result = splitter.split_documents(xs)

    if seed_id != -1:
        uuid_generator = UuidGenerator(seed_id)

        for doc in result:
            doc.id = uuid_generator.next()
    
    return result

def load_and_split(
        filepath: str, 
        loader = None, 
        splitter = None, 
        seed_id: Optional[int] = -1,
        flatten = True,
    ):
    partial_result = load_document(filepath=filepath, 
                         loader=loader, 
                         seed_id=seed_id)
    
    result = [
        split_document(x, splitter=splitter, seed_id=seed_id)
        for x in partial_result
    ]

    if flatten:
        return [
            y
            for x in result
            for y in x
        ]
    
    return result


_sentence_transformer_obj = None
def SentenceTransformer(*args, **kwargs):
    """
    Default args:
        - model: sentence-transformers/all-mpnet-base-v2
        - device: auto (cuda if available)
    """
    global _sentence_transformer_obj
    if _sentence_transformer_obj is None:
        from sentence_transformers import SentenceTransformer
        _sentence_transformer_obj = SentenceTransformer

    sig = inspect.signature(_sentence_transformer_obj)

    bound_args = sig.bind(*args, **kwargs)
    bound_args.apply_defaults()
    bound_args = bound_args.arguments
    
    if bound_args['model_name_or_path'] is None:
        bound_args["model_name_or_path"] = 'sentence-transformers/all-mpnet-base-v2'

    device = bound_args['device'] or 'auto'

    match device:
        case 'auto':
            bound_args['device'] = 'cuda' if is_cuda_available() else 'cpu'
        case 'cuda':
            if not is_cuda_available():
                raise ValueError("CUDA is not available. Use 'cpu' instead.")
        case 'cpu':
            pass
        case _:
            raise ValueError(f"Invalid device '{device}', expected 'cpu', 'cuda' or 'auto.")

    return _sentence_transformer_obj(**bound_args)

def encode_with_multiprocessing(transformer, pool):
    assert isinstance(transformer, type(SentenceTransformer()))
    assert set(pool.keys()) == {'input', 'output', 'processes'}, f"Expected: {{'input', 'output' 'processes'}}, got = {set(pool.keys())}"
    def _(x):
        result = transformer.encode_multi_process(x, pool=pool)
        transformer.stop_multi_process_pool(pool)
        return result
    return _

@allow_opaque_constructor(sentence_transformer = SentenceTransformer)
def vectorize_document(
        x: str | Document | Iterable[Document | str], 
        sentence_transformer = None,
        uid = None, 
        additional_metadata = dict(),
        devices = None
    ):
    
    devices = devices or ['cuda' if is_cuda_available() else 'cpu']
    
    generator: UuidGenerator
    if uid is None:
        generator = UuidGenerator()

    elif isinstance(uid, UuidGenerator):
        generator = uid
    
    else:
        raise ValueError
    
    uid = generator.next()

    if sentence_transformer is None:
        sentence_transformer = SentenceTransformer()

    encode: Callable
    if len(devices) <= 1:
        encode = sentence_transformer.encode
    else:
        pool = sentence_transformer.start_multi_process_pool(devices)
        encode = encode_with_multiprocessing(sentence_transformer, pool)

    if isinstance(x, str):
        return [dict(
            page_content = x,
            metadata = {}|additional_metadata,
            id = uid,
            embedding = encode(x)
        )]
    
    if isinstance(x, Document):
        return [dict(
            page_content = x.page_content,
            metadata = x.metadata|additional_metadata,
            id = x.id,
            embedding = encode(x.page_content)
        )]

    if isinstance(x, Iterable):
        t = reduce(union, map(type, x))
        assert t in (str, Document)
        
        if t == str:
            all_documents = x
            all_metadatas: list[dict] = [dict() for _ in x]
        elif t == Document:
            all_documents, all_metadatas = \
                zip(*((y.page_content, y.metadata) 
                      for y in x 
                      if isinstance(y, Document) # my-py no detecta el tipo
                    ))
        all_ids = [x for x in generator.map(all_documents)]
        all_embeddings = encode(all_documents)

        result = [
            dict(page_content = doc_i, 
                 metadata = metadata_i, 
                 id = uid_i, 
                 embedding = embedding_i)
            for (doc_i, metadata_i, uid_i, embedding_i)
            in zip(
                all_documents,
                all_metadatas,
                all_ids,
                all_embeddings
            )
        ]

        assert ((isinstance(x, Sized) and len(result) == len(x)) or 
                (isinstance(x, Iterable) and len(result) == len([y for y in x])))
        assert len(all_ids) == len(set(all_ids)), "IDs were not unique. Please try again with a new seed."

        return result
    
# VRAM

def available_vram_nvidia_smi():
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=memory.total,memory.free', '--format=csv,noheader,nounits'],
            stdout=subprocess.PIPE,
            encoding='utf-8'
        )
        output = result.stdout.strip()
        total_mem, free_mem = map(int, output.split(','))
        return free_mem * 1024 * 1024, total_mem * 1024 * 1024  # Convert MB to bytes
    except FileNotFoundError:
        pass

    raise RuntimeError("nvidia-smi not found. Ensure NVIDIA drivers are installed.")

def available_vram_torch():
    if torch.cuda.is_available():
        torch.cuda.synchronize()
        total_mem = torch.cuda.get_device_properties(0).total_memory
        allocated_mem = torch.cuda.memory_allocated(0)  # Memory currently allocated by tensors
        reserved_mem = torch.cuda.memory_reserved(0)  # Memory reserved by the CUDA allocator
        free_mem = reserved_mem - allocated_mem  # Available memory from reserved pool
        return free_mem, total_mem
    else:
        raise RuntimeError("CUDA is not available.")
    
def get_available_vram():
    try:
        return available_vram_nvidia_smi()
    except Exception as ex:
        pass
    
    try:
        return available_vram_torch()
    except Exception as ex:
        pass
    
    raise RuntimeError("Coudlnt get available memory.")


# Models

def splitmodel(x) -> tuple[str, str]:
    if ':' not in x:
        return x, ''
    
    model, specs = x.split(':')
    return model, specs

def modelname(x):
    return splitmodel(x)[0]

def modelspecs(x):
    return splitmodel(x)[1]