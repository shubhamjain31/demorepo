# Generated by Django 2.2.12 on 2022-03-13 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information_name', models.CharField(blank=True, max_length=200, null=True)),
                ('json_text_field', models.TextField(default='{}')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Informations')),
            ],
        ),
    ]
