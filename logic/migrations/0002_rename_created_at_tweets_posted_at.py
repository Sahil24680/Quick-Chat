# Generated by Django 5.0.6 on 2024-06-02 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweets',
            old_name='created_at',
            new_name='posted_at',
        ),
    ]
