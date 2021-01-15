# Generated by Django 3.1.2 on 2020-12-29 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_userblog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userblog',
            name='event_user',
        ),
        migrations.RemoveField(
            model_name='userblog',
            name='user_post',
        ),
        migrations.AddField(
            model_name='post',
            name='user_blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Blog.userblog'),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='avatar_user',
            field=models.ImageField(blank=True, upload_to='avatar/'),
        ),
    ]
