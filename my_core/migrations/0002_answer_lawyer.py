# Generated by Django 5.1 on 2024-10-17 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_core', '0001_initial'),
        ('my_users', '0002_lawyer_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='lawyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='my_users.lawyer'),
        ),
    ]
