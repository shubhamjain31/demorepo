# Generated by Django 3.1 on 2021-06-13 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pyment',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pyment',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]