# Generated by Django 3.1.2 on 2020-12-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_userblog_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_post',
            field=models.ManyToManyField(related_name='people_liked', to='Blog.UserBlog'),
        ),
    ]