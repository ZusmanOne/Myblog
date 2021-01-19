from django.shortcuts import render
from .models import Post
#from .forms import PostForm


def home(request):
    return(render(request, 'Blog/base.html'))

def ShowPost(request):
    blog_post = Post.objects
    return render(request, 'Blog/blog.html',{'myblog':blog_post})

#def post_new(request):
 #   form = PostForm()
  #  return render(request,'Blog/Blog/create_post.html',{'form': form})

from django.views.generic.edit import CreateView

class PostCreate(CreateView):
    model = Post
    fields = '__all__'


# Create your views here.
