# Generated by Django 4.0.6 on 2022-10-24 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studio', '0007_merge_20221024_1207'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0005_alter_user_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'like',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(default='1', max_length=2)),
                ('photoUrl', models.CharField(default='url', max_length=500)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_photos', through='photo.Like', to=settings.AUTH_USER_MODEL)),
                ('studio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studio.studio')),
            ],
            options={
                'db_table': 'photo',
            },
        ),
        migrations.AddField(
            model_name='like',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.photo'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
