from langchain.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from collections.abc import Iterable, Sized
from typing import Optional
from functools import reduce
from operator import or_ as union
from typing import TypeVar, Callable
from fundar_llms.utils.uuid import UuidGenerator
from fundar_llms.utils.common import allow_opaque_constructor
from ..cuda import is_cuda_available
import inspect


T = TypeVar('T')

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
        from sentence_transformers import SentenceTransformer # type: ignore
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
