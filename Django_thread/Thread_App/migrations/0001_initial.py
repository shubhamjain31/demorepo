# Generated by Django 3.2.4 on 2021-07-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
