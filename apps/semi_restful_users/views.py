from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'semi_restful_users/index.html')

def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'semi_restful_users/users.html', context)

def new(request):
    return render(request, 'semi_restful_users/new_user.html')

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect('/users')

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'semi_restful_users/show_user.html', context)

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'semi_restful_users/edit_user.html', context)

def update(request):
    user = User.objects.get(id=request.POST['id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/user/' + request.POST['id'])
