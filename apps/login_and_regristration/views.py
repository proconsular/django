from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    if 'user' in request.session:
        return redirect('/user')
    return render(request, 'login_and_regristration/index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validateRequest(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        users = User.objects.filter(email=request.POST['email'])
        if len(users) > 0:
            messages.error(request, "Email already in use.")
            return redirect('/')
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        user.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user.save()
        messages.success(request, "You've successfully registered.")
    return redirect('/')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if len(user) == 0:
            messages.error(request, "Invalid login.")
            return redirect('/')
        user = user[0]
        if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            messages.error(request, "Invalid login.")
            return redirect('/')
        request.session["user"] = user.id
        return redirect('/user')
    return redirect('/')

def user(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=int(request.session['user'])),
        'users': User.objects.all()
    }
    return render(request, 'login_and_regristration/user.html', context)

def logout(request):
    del request.session['user']
    request.session.modified = True
    return redirect('/')
