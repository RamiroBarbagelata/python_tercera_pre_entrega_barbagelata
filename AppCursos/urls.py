from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("view_courses", views.view_courses, name="courses"),
    path("students", views.students, name="students"),
    path("course_registration", views.course_form),
    path("search_course", views.search_course),
    path("search", views.search),
    path("delete_course/<int:id>", views.delete_course, name="delete_course"),
    path("edit_course/<int:id>", views.edit_course, name="edit_course"),
    path("new_students", views.students_form, name="new_students"),
    path("view_students" , views.view_students , name = "students"),
    path("new_professors", views.professors_form, name="new_professors"),
    path("view_professors" , views.view_professors , name = "professors")
    
]