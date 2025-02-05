from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet


router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]

# api-token-auth/ (POST): передаём логин и пароль, получаем токен.

# posts/ (GET, POST): получаем список всех постов или создаём новый пост.
# posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост с идентификатором`{post_id}`.

# groups/ (GET): получаем список всех групп.
# groups/{group_id}/ (GET): получаем информацию о группе с идентификатором `{group_id}`.

# posts/{post_id}/comments/ (GET): получаем список всех комментариев поста с идентификатором `{post_id}`.
# posts/{post_id}/comments/ (POST): создаём новый комментарий для поста с идентификатором `{post_id}`.
# posts/{post_id}/comments/{comment_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий.

# В ответ на запросы POST, PUT и PATCH ваш API должен возвращать объект, который был добавлен или изменён.
