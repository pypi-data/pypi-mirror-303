_umap = None
def UMAP(*args, **kwargs):
    global _umap
    if _umap is None:
        from umap.umap_ import UMAP
        _umap = UMAP
    return _umap(*args, **kwargs)