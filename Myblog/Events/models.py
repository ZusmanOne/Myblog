from django.db import models

class Event(models.Model):
    event_images = models.ImageField(upload_to = 'event-images/')
    event_text = models.CharField(max_length = 300)
    event_name = models.CharField(max_length=50, null=True)



# Create your models here.
