# Generated by Django 4.0.6 on 2022-12-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, '프로필 사진'), (2, '증명 사진'), (3, '단체 사진'), (4, '컨셉 사진')], default=1, null=True),
        ),
    ]
