from django.db import models

# Create your models here.

class Course(models.Model):
    
    course_name = models.CharField(max_length=40)
    commission  = models.IntegerField()
    
    def __str__(self):
        return f"Curso: {self.course_name}      Comisión: {self.commission}"
    
    
class Students(models.Model):
    students_name = models.CharField(max_length=40)
    students_lastname = models.CharField(max_length=40)
    file_number  = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.students_name}      Apellido: {self.students_lastname}     Nº de Legajo: {self.file_number}  "
    
class Professors(models.Model):
    professors_name = models.CharField(max_length=40)
    professors_lastname= models.CharField(max_length=40)
    file_number = models.IntegerField()
    
    
    def __str__(self):
        return f"Nombre: {self.professors_name}      Apellido: {self.professors_lastname}     Nº de Legajo: {self.file_number}  "