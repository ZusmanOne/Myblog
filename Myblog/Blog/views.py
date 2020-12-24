from django.shortcuts import render
from .models import Post

def ShowPost(request):
    blog_post = Post.objects
    return render(request, 'Blog/blog.html',{'myblog':blog_post})

# Create your views here.
