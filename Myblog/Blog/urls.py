from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowPost, name = 'posts'),
    path(r'post/create/', views.PostCreate.as_view(), name = 'post_create'),
]
