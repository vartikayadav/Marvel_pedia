# Generated by Django 2.0.7 on 2019-03-16 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0002_comics_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comics',
            name='image',
        ),
    ]
