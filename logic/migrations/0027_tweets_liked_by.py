# Generated by Django 5.0.6 on 2024-06-14 03:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0026_tweets_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_tweets', to=settings.AUTH_USER_MODEL),
        ),
    ]
