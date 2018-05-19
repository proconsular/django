from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        Course.objects.create(name=request.POST['name'],description=request.POST['description'])
        messages.success(request, "Course successfully added.")
    return redirect('/')

def confirm(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'courses/destroy.html', context)

def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')
