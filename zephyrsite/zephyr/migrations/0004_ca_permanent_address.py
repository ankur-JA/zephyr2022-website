# Generated by Django 3.2.5 on 2023-01-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zephyr', '0003_auto_20230103_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='ca',
            name='permanent_address',
            field=models.TextField(default=''),
        ),
    ]