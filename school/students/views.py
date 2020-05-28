from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student

# Create your views here.

    
def students(request):
    student = Student.objects.order_by('roll_no')
    return render(request, 'students/students.html', {'student': student})

def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    html.set_cookie('dataflair', 'Hello this is your Cookies', max_age = None)
    return html
       