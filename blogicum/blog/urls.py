from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # View posts.
    path('',
         views.PostIndexListView.as_view(), name='index'),
    path('category/<slug:category_slug>/',
         views.PostCategoryListView.as_view(), name='category_posts'),
    path('posts/<int:post_id>/',
         views.PostDetailView.as_view(), name='post_detail'),

    # Edit posts.
    path('posts/create/',
         views.PostCreateView.as_view(), name='create_post'),
    path('posts/<int:post_id>/edit/',
         views.PostUpdateView.as_view(), name='edit_post'),
    path('posts/<int:post_id>/delete/',
         views.PostUpdateView.as_view(), name='delete_post'),

    # Profile.
    path('profile/<str:username>/',
         views.ProfileListView.as_view(), name='profile'),
    path('edit_profile/',
         views.ProfileUpdateView.as_view(), name='edit_profile'),
]
