# Generated by Django 5.1 on 2024-11-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_core', '0004_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')]),
        ),
    ]
