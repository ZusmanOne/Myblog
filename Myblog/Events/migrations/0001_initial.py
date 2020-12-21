# Generated by Django 3.1.2 on 2020-12-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_images', models.ImageField(upload_to='event-images/')),
                ('event_text', models.CharField(max_length=300)),
            ],
        ),
    ]