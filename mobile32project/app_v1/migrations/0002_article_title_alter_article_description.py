# Generated by Django 4.2.6 on 2023-10-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_v1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.TextField(default='Title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(default='Description'),
        ),
    ]
