# Generated by Django 4.0.6 on 2022-10-25 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photoUrl',
            new_name='photo_url',
        ),
    ]
