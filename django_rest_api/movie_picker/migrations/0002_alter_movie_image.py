# Generated by Django 4.1.7 on 2023-03-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_picker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.URLField(),
        ),
    ]
