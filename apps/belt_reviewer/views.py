from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    if 'user' in request.session:
        return redirect('/books')
    return render(request, 'belt_reviewer/index.html')

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
        return redirect('/books')
    return redirect('/')

def user(request):
    if 'user' not in request.session:
        return redirect('/')
    reviews = Review.objects.all().order_by('-created_at')[:3]
    context = {
        'user': User.objects.get(id=int(request.session['user'])),
        'users': User.objects.all(),
        'reviews': reviews,
        'other_reviews': Review.objects.all().order_by('-created_at')[3:],
        'range': range(0, 5)
    }
    return render(request, 'belt_reviewer/user.html', context)

def book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'range': range(0, 5)
    }
    return render(request, 'belt_reviewer/book.html', context)

def add_review(request):
    if request.method == "POST":
        Review.objects.create(content=request.POST['content'], rating=int(request.POST['rating']), book_id=request.POST['book_id'], user_id=request.session['user'])
    return redirect('/books/' + request.POST['book_id'])

def profile(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': user,
        'review_count': len(user.reviews.all())
    }
    return render(request, 'belt_reviewer/profile.html', context)

def logout(request):
    del request.session['user']
    request.session.modified = True
    return redirect('/')

def add(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'belt_reviewer/add.html', context)

def create(request):
    if request.method == "POST":
        author = None
        if request.POST['author'] == "none":
            author = Author.objects.create(first_name=request.POST['author_first_name'], last_name=request.POST['author_last_name'])
        else:
            author = Author.objects.get(id=int(request.POST['author']))
        author.save()
        book = Book.objects.create(name=request.POST['name'], author_id=author.id)
        book.save()
        review = Review.objects.create(content=request.POST['review'], rating=int(request.POST['rating']), book_id=book.id, user_id=request.session['user'])
        review.save()
    return redirect('/books')
