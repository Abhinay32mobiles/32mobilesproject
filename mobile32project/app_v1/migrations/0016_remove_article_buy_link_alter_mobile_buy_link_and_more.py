# Generated by Django 4.2.6 on 2023-10-10 09:01

import app_v1.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_v1', '0015_alter_article_buy_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='buy_link',
        ),
        migrations.AlterField(
            model_name='mobile',
            name='buy_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(blank=True, null=True), default=app_v1.models.default_buy_link, size=3),
        ),
        migrations.AlterField(
            model_name='pc',
            name='buy_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(blank=True, null=True), default=app_v1.models.default_buy_link, size=3),
        ),
    ]
