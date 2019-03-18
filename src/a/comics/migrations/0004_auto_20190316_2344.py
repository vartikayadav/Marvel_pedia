# Generated by Django 2.0.7 on 2019-03-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0003_remove_comics_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comics',
            options={'ordering': ['title'], 'verbose_name': 'comic', 'verbose_name_plural': 'comics'},
        ),
        migrations.AddField(
            model_name='comics',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comics',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='comics',
            name='image',
            field=models.ImageField(blank=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='comics',
            name='slug',
            field=models.SlugField(max_length=256, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='comics',
            name='stock',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='comics',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='comics',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]