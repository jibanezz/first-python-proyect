from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def umairurl(request):
    return render (request, 'umairurl.html')


from .models import Fruit

def fruits(request):
    fruits_list = Fruit.objects.all()
    return render(request, 'fruits.html',{'flist' : fruits_list})

from.models import Student

def students(request):
    students_list = Student.objects.all()
    return render(request, 'students.html',{'slist' : students_list})