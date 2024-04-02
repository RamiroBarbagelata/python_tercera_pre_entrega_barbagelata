from django import forms


class Course_form(forms.Form):

    course_name = forms .CharField(max_length=30)
    commission = forms .IntegerField()
    
class Students_form(forms.Form):

    students_name = forms .CharField(max_length=30)
    students_lastname = forms .CharField(max_length=30)
    file_number = forms .IntegerField()

class Professors_form(forms.Form):

    professors_name = forms .CharField(max_length=30)
    professors_lastname = forms .CharField(max_length=30)
    file_number = forms .IntegerField()  
