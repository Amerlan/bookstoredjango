# Generated by Django 3.1.3 on 2020-12-01 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201201_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='transaction',
        ),
    ]
