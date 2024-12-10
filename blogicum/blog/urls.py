from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path(
        '', views.PostIndexListView.as_view(),
        name='index'),
    path(
        'category/<slug:category_slug>/', views.PostCategoryListView.as_view(),
        name='category_posts'
    ),
    path(
        'posts/<int:post_id>/', views.PostDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'profile/<str:username>/', views.ProfileListView.as_view(),
        name='profile'
    ),
    path(
        'edit_profile/', views.ProfileUpdateView.as_view(),
        name='edit_profile'
    ),
]
