from .posts import (
    PostIndexListView, PostCategoryListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)
from .profiles import (
    ProfileListView, ProfileUpdateView
)


__all__ = [
    PostIndexListView, PostCategoryListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,

    ProfileListView, ProfileUpdateView
]
