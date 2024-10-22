from .tsne import *
from .umap import *
from .projections import project_data

"""
Usage:

```
from fundar_llms.dimred import TSNE, UMAP, project_data

umap_transform = UMAP(
    random_state = 0,
    transform_seed = 0,
    metric = 'cosine',
)

tsne_transform = TSNE(
    random_state = 0,
    metric = 'cosine',
)

umap_transform = umap_transform.fit(data)
tsne_transform = tsne.fit(data)

projected_umap = project_data(umap_transform, data)
projected_tsne = project_data(tsne_transform, data)
```
"""