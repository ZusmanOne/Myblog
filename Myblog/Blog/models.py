from django.db import models

from Events.models import Event


class UserBlog(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=False)
    e_mail = models.EmailField(help_text='vvedite po4tu')
    avatar_user = models.ImageField(upload_to='avatar/', blank=True)
    event_user = models.ManyToManyField(Event)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Post(models.Model):
    post_title = models.CharField(max_length=300)
    post_date = models.DateTimeField(auto_now=False)
    post_text = models.CharField(max_length=1000)
    post_image = models.ImageField(upload_to='postimage/', null=True, blank=True)
    user_blog = models.ForeignKey(UserBlog, on_delete=models.SET_NULL, null=True, related_name='writing_post')
    like_post = models.ManyToManyField(UserBlog, related_name='people_liked')

    def __str__(self):
        return self.post_title

# Create your models here.
