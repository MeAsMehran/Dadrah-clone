# Generated by Django 5.1 on 2024-11-20 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_core', '0006_scrapedquestion_scrapedanswer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ScrapedAnswer',
        ),
        migrations.DeleteModel(
            name='ScrapedQuestion',
        ),
    ]
