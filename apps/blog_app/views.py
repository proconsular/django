from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    response = "Hello, I am your first requestd!"
    return HttpResponse(response)

def new(request):
    response = "New"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse("Number: " + number)

def edit(request, number):
    return HttpResponse("Edit: " + number)

def delete(request, number):
    return HttpResponse("Delete: " + number)
