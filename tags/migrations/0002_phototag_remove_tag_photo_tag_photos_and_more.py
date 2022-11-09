# Generated by Django 4.0.6 on 2022-11-09 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_photo_price'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.photo')),
            ],
        ),
        migrations.RemoveField(
            model_name='tag',
            name='photo',
        ),
        migrations.AddField(
            model_name='tag',
            name='photos',
            field=models.ManyToManyField(related_name='tags', through='tags.PhotoTag', to='photo.photo'),
        ),
        migrations.DeleteModel(
            name='Photo_Tag',
        ),
        migrations.AddField(
            model_name='phototag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.tag'),
        ),
    ]
