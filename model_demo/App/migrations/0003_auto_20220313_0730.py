# Generated by Django 2.2.12 on 2022-03-13 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_images_informations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informations',
            name='json_text_field',
            field=models.TextField(default='[]'),
        ),
    ]
