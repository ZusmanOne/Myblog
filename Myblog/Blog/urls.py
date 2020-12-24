from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowPost, name = 'posts'),
]
