# Generated by Django 3.2.3 on 2021-07-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'test_blog',
            },
        ),
        migrations.CreateModel(
            name='test_employee',
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
            options={
                'db_table': 'test_employee',
            },
        ),
    ]
