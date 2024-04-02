from django.shortcuts import render
from AppCursos.models import Course, Students, Professors
from django.http import HttpResponse
from django.template import loader
from AppCursos.forms import Course_form, Students_form, Professors_form

# Create your views here.

def home(request):
    return render(request, "padre.html")

def course_registration(request, course_name):
    course = Course(course_name=course_name, commission=12345)
    course.save()
    text = f"Se guardo en la BD el curso: {course.course_name} {course.commission}"
    return HttpResponse(text)

def view_courses(request):
    courses = Course.objects.all()
    dicc = {"courses": courses}
    template = loader.get_template("courses.html")
    document = template.render(dicc)
    return HttpResponse(document)

def students(request):
    return render(request, "students.html")

def course_form(request):

    if request.method == "POST":
        my_form = Course_form(request.POST)
        
        if my_form.is_valid():
            data = my_form.cleaned_data
            course = Course(course_name = data["course_name"], commission = data["commission"])
            course.save()
            return render(request, "course_form.html")
    
    return render(request, "course_form.html")

def search_course(request):
    return render(request, "search_course.html")


def search(request):
    if request.GET["course_name"]:
        course_name = request.GET["course_name"]
        courses = Course.objects.filter(course_name__icontains=course_name)
        return render (request, "search_result.html", {"courses": courses})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    
def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    
    course = Course.objects.all()
    
    return render(request, "courses.html", {"courses": course})


def edit_course(request , id):

    course = Course.objects.get(id=id)

    if request.method == "POST":

        my_form = Course_form( request.POST )
        if my_form.is_valid():
            data = my_form.cleaned_data
            course.course_name = data["course_name"]
            course.commission = data["commission"]
            course.save()

            course = Course.objects.all()

            return render(request , "courses.html" , {"courses":course})


        
    else:
        my_form = Course_form(initial={"course_name":course.course_name , "commission":course.commission})
    
    return render( request , "edit_course.html" , {"my_form": my_form , "course":course})

def new_students(request , students_name  , students_lastname , file_number):
    student = Students(students_name=students_name, students_lastname=students_lastname , file_number=file_number)
    student.save()
    text = f"Se guardó en la Base de Datos el Alumno: {student.students_name} {student.students_lastname} ({student.file_number})"
    return HttpResponse(text)

def view_students(request):
    students = Students.objects.all()
    dicc = {"students" : students}
    template = loader.get_template("students.html")
    document = template.render(dicc)
    return HttpResponse(document)


def students_form(request):
    
    if request.method == "POST":
        my_form = Students_form(request.POST)
        
        if my_form.is_valid():
            data = my_form.cleaned_data
            student = Students(students_name = data["students_name"], students_lastname = data["students_lastname"], file_number = data["file_number"])
            student.save()
            return render(request , "students_form.html")
            
    return render(request , "students_form.html") 

# PROFESSORS

def new_professors(request , professors_name  , professors_lastname , file_number):
    professor = Professors(professors_name =professors_name, professors_lastname=professors_lastname , file_number =file_number)
    professor.save()
    text = f"Se guardó en la Base de Datos de profesores: {professor.professors_name} {professor.professors_lastname} ({professor.file_number})"
    return HttpResponse(text)

def view_professors(request):
    professors = Professors.objects.all()
    dicc = {"professors" : professors}
    template = loader.get_template("professors.html")
    document = template.render(dicc)
    return HttpResponse(document)


def professors_form(request):
    
    if request.method == "POST":
        my_form = Professors_form(request.POST)
        
        if my_form.is_valid():
            data = my_form.cleaned_data
            professor = Professors(professors_name = data["professors_name"], professors_lastname = data["professors_lastname"], file_number = data["file_number"])
            professor.save()
            return render(request , "professors_form.html")
            
    return render(request , "professors_form.html") 


