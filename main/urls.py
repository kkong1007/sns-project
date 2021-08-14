from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('show/', show),
    path('bucket/', bucket, name="bucket"),
    path('photo/', photo, name="photo"),
    path('<str:id>',detail, name="detail"),
    path('new/', new, name="new"),
    path('posts/', posts, name="posts"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
    path('<str:post_id>/create_comment', create_comment, name="create_comment"),
    path('edit_comment/<str:comment_id>', edit_comment, name="edit_comment"),
    path('update_comment/<str:comment_id>', update_comment, name="update_comment"),
    path('delete_comment/<str:comment_id>', delete_comment, name="delete_comment"),

    # 1. like_toggle url 연결하기
    path('like_toggle/<int:post_id>/', like_toggle,name="like_toggle"),
    # 2. dislike
    path('dislike_toggle/<int:post_id>/', dislike_toggle,name="dislike_toggle"),
]