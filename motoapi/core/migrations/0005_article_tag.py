# Generated by Django 4.2.6 on 2023-10-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='core.tag'),
        ),
    ]
