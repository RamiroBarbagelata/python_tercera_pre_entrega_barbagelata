# Generated by Django 5.0.3 on 2024-04-01 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCursos', '0003_professor_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Professors',
        ),
        migrations.RenameModel(
            old_name='Professor',
            new_name='Students',
        ),
        migrations.RenameField(
            model_name='professors',
            old_name='student_name',
            new_name='professors_name',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='professor_name',
            new_name='students_name',
        ),
    ]
