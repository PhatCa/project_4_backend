# Generated by Django 4.1.7 on 2023-03-25 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_picker', '0002_alter_movie_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='realease_date',
            new_name='release_date',
        ),
    ]
