from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from django.utils import timezone

from .models import Post, Category


def index(request):
    """Выводятся пять последних публикаций.

    На главной странице должны показываться только те публикации,
    у которых одновременно:
    1. Дата публикации — не позже текущего времени
    2. Значение поля is_published равно True
    3. У категории, к которой принадлежит публикация,
       значение поля is_published равно True.
    """
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        Q(category__is_published__exact=True)
        & Q(is_published__exact=True)
        & Q(pub_date__lte=timezone.now())
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    """Выводится отдельная публикация, полученная по первичному ключу.

    Запрос к странице публикации должен вернуть ошибку 404, если:
    1. Дата публикации — позже текущего времени
    2. Или значение поля is_published у запрошенной публикации равно False
    3. Или у категории, к которой принадлежит публикация,
       значение поля is_published равно False
    """
    template = 'blog/detail.html'
    post = get_object_or_404(Post, pk=post_id)
    if not (
        post.pub_date < timezone.now()
        and post.is_published
        and post.category.is_published
    ):
        return HttpResponseNotFound(f'Post with id {post_id} not found.')
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Выводятся публикации выбранной категории.

    Выводятся только те публикации, которые
    1. Принадлежат выбранной категории
    2. Значение поля is_published равно True
    3. Дата публикации — не позже текущего времени.
    Если у запрошенной категории значение поля is_published равно
    False — должна возвращаться ошибка 404.
    """
    template = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug)
    if not category.is_published:
        return HttpResponseNotFound(f'Category {category_slug} not found.')

    post_list = Post.objects.filter(
        Q(category__exact=category)
        & Q(is_published__exact=True)
        & Q(pub_date__lte=timezone.now())
    ).order_by('-pub_date')
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
