# Generated by Django 3.2.3 on 2021-08-07 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_student', to='App.student'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_teacher', to='App.teacher'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='students',
            field=models.ManyToManyField(related_name='student_courses', to='App.Student'),
        ),
    ]
