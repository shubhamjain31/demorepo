# Generated by Django 2.2.12 on 2022-04-16 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_quiz_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='fee',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
