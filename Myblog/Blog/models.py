from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length = 300)
    post_date = models.DateTimeField(auto_now=False)
    post_text = models.CharField(max_length = 1000)
    post_image = models.ImageField(upload_to = 'postimage/')

# Create your models here.
