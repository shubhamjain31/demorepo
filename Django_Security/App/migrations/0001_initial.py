# Generated by Django 3.2.3 on 2021-07-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=1000)),
                ('last_name', models.CharField(max_length=1000)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=1000)),
                ('designation', models.CharField(max_length=1000)),
            ],
        ),
    ]
