# Generated by Django 4.2.6 on 2023-10-12 11:18

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_tag_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=core.models.thumbnail_file_path),
        ),
    ]