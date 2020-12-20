# Generated by Django 3.1.3 on 2020-11-21 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='author name')),
                ('dob', models.DateField(verbose_name="author's date of birth")),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('img', models.ImageField(upload_to='', verbose_name='book photo')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.author')),
            ],
        ),
    ]
