from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator


def index(request):
    
    peoples = [
        {'name': 'Bhavesh Ramani', 'age': 21},
        {'name': 'Aastha sharma', 'age': 20},
        {'name': 'Ram ', 'age': 10},
        {'name': 'shyam', 'age': 18},
        {'name': 'Krishna ji', 'age': 15},
        {'name': 'Radha ji', 'age': 22},
    ]
    return render(request, 'index.html', context={'peoples' : peoples})

def home(request):
    return HttpResponse("hey welcome to my new project")

def success_page(request):
    return HttpResponse("<h1> this is a success page</h1>")


def get_students(request):
    queryset = Student.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        print("Search query:", search)
        queryset = queryset.filter(student_name__icontains=search)
        print("Filtered queryset:", queryset)
          
    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    print(page_obj.object_list)
    return render(request, 'report/student.html', {'queryset' : page_obj})



 