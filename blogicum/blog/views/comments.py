from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post, Comment
from blog.forms import CommentForm


class CommentMixin(LoginRequiredMixin):
    """Set default model and template for comment views."""

    model = Comment
    template_name = 'blog/comment.html'
    _post = None

    def get_success_url(self):
        """Return post detail page (blog:post_detail)."""
        return reverse('blog:post_detail', kwargs={'post_id': self._post.pk})


class CommentCreateView(CommentMixin, CreateView):
    """Create comment."""

    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        """Get post object or 404."""
        self._post = get_object_or_404(
            Post, pk=kwargs['post_id'],
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Save model instance."""
        form.instance.author = self.request.user
        form.instance.post = self._post
        return super().form_valid(form)


# Could've used a mixin for CommentDeleteView and CommentUpdateView,
# but checking for the existence of the required methods, objects and args
# to ensure security would be overly complicated.
class CommentUpdateView(CommentMixin, UpdateView):
    """Edit an existing comment text."""

    form_class = CommentForm
    pk_url_kwarg = 'comment_id'

    def dispatch(self, request, *args, **kwargs):
        """Check if the current user is the author of the comment."""
        self._post = self.get_object().post
        if self._post.author != request.user:
            return redirect('blog:post_detail', id=self.kwargs['post_id'])
        return super().dispatch(request, *args, **kwargs)


class CommentDeleteView(CommentMixin, DeleteView):
    """Delete an existing comment."""

    pk_url_kwarg = 'comment_id'

    def dispatch(self, request, *args, **kwargs):
        """Check if the current user is the author of the comment."""
        self._post = self.get_object().post
        if self._post.author != request.user:
            return redirect('blog:post_detail', id=self.kwargs['post_id'])
        return super().dispatch(request, *args, **kwargs)
