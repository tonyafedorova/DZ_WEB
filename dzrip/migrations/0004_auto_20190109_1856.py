# Generated by Django 2.1.3 on 2019-01-09 18:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dzrip', '0003_picture_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='author',
        ),
        migrations.AddField(
            model_name='picture',
            name='author',
            field=models.CharField(default='Не указан', max_length=100, verbose_name='Автор'),
        ),
        migrations.RemoveField(
            model_name='picture',
            name='like',
        ),
        migrations.AddField(
            model_name='picture',
            name='like',
            field=models.ManyToManyField(blank=True, default=0, to=settings.AUTH_USER_MODEL, verbose_name='Лайки'),
        ),
    ]
