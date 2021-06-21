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
]