# Generated by Django 4.0.6 on 2022-10-25 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0010_rename_closetime_studio_close_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studioimage',
            name='studio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studio_images', to='studio.studio'),
        ),
    ]