# Generated by Django 3.1.3 on 2020-12-03 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20201201_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=None, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.CharField(default=None, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='zipCode',
            field=models.CharField(default=None, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.PositiveSmallIntegerField(verbose_name='price'),
        ),
    ]