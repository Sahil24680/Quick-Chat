# Generated by Django 5.0.6 on 2024-06-12 14:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0021_alter_tweets_tweet_alter_tweets_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='tweet',
            field=models.CharField(max_length=280),
        ),
        migrations.AlterField(
            model_name='tweets',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
