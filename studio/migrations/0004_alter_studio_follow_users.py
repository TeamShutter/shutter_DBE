# Generated by Django 4.0.6 on 2022-11-08 10:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
        ('studio', '0003_alter_studio_address_alter_studio_close_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='follow_users',
            field=models.ManyToManyField(blank=True, related_name='studio_follows', through='studio.Follow', to=settings.AUTH_USER_MODEL),
        ),
    ]
