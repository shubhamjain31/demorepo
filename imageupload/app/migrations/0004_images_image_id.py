# Generated by Django 3.0.1 on 2019-12-29 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image_id',
            field=models.CharField(default='', max_length=10),
        ),
    ]
