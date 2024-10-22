from tqdm.auto import tqdm
from fundar_llms.dimred.umap import UMAP
from fundar_llms.dimred.tsne import TSNE
from numpy import empty as empty_vector

def umap_project_embeddings(umap_transform, embeddings, show_progress, strict: bool, dimensions: int):
    assert isinstance(umap_transform, type(UMAP()))

    if strict:
        umap_embeddings = empty_vector((len(embeddings), dimensions))
        for i,embedding in enumerate(tqdm(embeddings, disable=(not show_progress))):
            umap_embeddings[i] = umap_transform.transform([embedding])
        return umap_embeddings
    else:
        return umap_transform.transform(embeddings)

def tsne_project_embeddings(tsne_transform, embeddings, show_progress):
    assert isinstance(tsne_transform, TSNE)
    
    tsne_transform.verbose = show_progress
    result = tsne_transform.fit_transform(embeddings)
    tsne_transform.verbose = False

    return result

def project_data(transform, 
                 embeddings, by: str = None, 
                 show_progress: bool = True,
                 strict: bool = True,
                 dimensions: int = 2
                 ):
    if by is None:
        by = 'tsne' if isinstance(transform, TSNE) else 'umap'
    
    match by:
        case 'tsne':
            return tsne_project_embeddings(transform, embeddings, show_progress)
        case 'umap':
            return umap_project_embeddings(transform, embeddings, show_progress, strict, dimensions)
        case _:
            raise TypeError(f"Unknown transform {type(transform)}")