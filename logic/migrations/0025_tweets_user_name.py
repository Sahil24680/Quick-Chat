# Generated by Django 5.0.6 on 2024-06-13 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0024_remove_tweets_user_tweets_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='user_name',
            field=models.CharField(default=0.00024703557312252963, max_length=29),
            preserve_default=False,
        ),
    ]
