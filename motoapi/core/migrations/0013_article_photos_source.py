# Generated by Django 4.2.6 on 2023-10-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_article_slug_alter_article_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photos_source',
            field=models.CharField(default='materiały producenta', max_length=255),
        ),
    ]