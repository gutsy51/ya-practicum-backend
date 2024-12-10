from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView

from blog.models import Post, Category


POSTS_PER_PAGE = 10


class PostIndexListView(ListView):
    """Show latest POSTS_PER_PAGE posts.

    1. Publication date must be earlier than current;
    2. Post & category must be published.
    """
    model = Post
    template_name = 'blog/index.html'
    paginate_by = POSTS_PER_PAGE

    def get_queryset(self):
        return self.model.objects.filter(
            category__is_published__exact=True, is_published__exact=True,
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class PostCategoryListView(ListView):
    """Show latest POSTS_PER_PAGE posts in category.

    1. Publication date must be earlier than current;
    2. Post & category must be published.
    3. Posts must belong to selected category.
    """
    model = Post
    template_name = 'blog/category.html'
    paginate_by = POSTS_PER_PAGE

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._category = None

    def get_category(self) -> Category:
        """Fetch and cache the category object."""
        if not self._category:
            self._category = get_object_or_404(
                Category,
                slug=self.kwargs['category_slug'],
                is_published=True
            )
        return self._category

    def get_queryset(self, **kwargs):
        """Return posts for <category_slug> category."""
        category = self.get_category()
        return self.model.objects.filter(
            category__exact=category,
            is_published__exact=True, pub_date__lte=timezone.now()
        ).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        """Add category to the context."""
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_category()
        return context


class PostDetailView(DetailView):
    """Show a single post by ID.

    1. Publication date must be earlier than current;
    2. Post & category must be published.
    """
    model = Post
    template_name = 'blog/detail.html'

    def get_object(self, **kwargs):
        """Return Post or Http404 by post ID."""
        return get_object_or_404(
            self.model.objects.filter(
                pub_date__lt=timezone.now(), is_published__exact=True,
                category__is_published__exact=True, pk=self.kwargs['post_id']
            )
        )
