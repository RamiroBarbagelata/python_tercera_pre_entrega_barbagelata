# Generated by Django 5.0.3 on 2024-04-01 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCursos', '0004_rename_student_professors_rename_professor_students_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professors',
            old_name='commission',
            new_name='file_number',
        ),
        migrations.RenameField(
            model_name='professors',
            old_name='course_name',
            new_name='professors_lastname',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='commission',
            new_name='file_number',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='course_name',
            new_name='students_lastname',
        ),
    ]
