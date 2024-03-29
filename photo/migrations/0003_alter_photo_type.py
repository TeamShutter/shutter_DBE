# Generated by Django 4.0.6 on 2022-12-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_photo_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'white'), (2, 'gray'), (3, 'black'), (4, 'pink'), (5, 'red'), (6, 'wheat'), (7, 'orange'), (8, 'yellow'), (9, 'greenyellow'), (10, 'olive'), (11, 'skyblue'), (12, 'navy'), (13, 'saddlebrown'), (14, 'purple')], default=1, null=True),
        ),
    ]
