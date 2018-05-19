from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from itertools import chain

def main(request):
    return redirect('/main')

def index(request):
    if 'user' in request.session:
        return redirect('/travels')
    return render(request, 'belt_exam/index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validateRequest(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/main')
        users = User.objects.filter(username=request.POST['username'])
        if len(users) > 0:
            messages.error(request, "Username already in use.")
            return redirect('/main')
        user = User.objects.create(name=request.POST['name'], username=request.POST['username'])
        user.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user.save()
        messages.success(request, "You've successfully registered.")
    return redirect('/main')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(username=request.POST['username'])
        if len(user) == 0:
            messages.error(request, "Invalid login.")
            return redirect('/main')
        user = user[0]
        if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            messages.error(request, "Invalid login.")
            return redirect('/main')
        request.session["user"] = user.id
        return redirect('/travels')
    return redirect('/main')

def travels(request):
    if 'user' not in request.session:
        return redirect('/main')
    user = User.objects.get(id=int(request.session['user']))
    trips = list(chain(user.created_trips.all(), user.joined_trips.all()))
    other_users = Trip.objects.exclude(creator_id=user.id).exclude(joined_users=user)
    context = {
        'user': user,
        'trips': trips,
        'other_trips': other_users
    }
    return render(request, 'belt_exam/user.html', context)

def logout(request):
    del request.session['user']
    request.session.modified = True
    return redirect('/main')

def destination(request, destination_id):
    if 'user' not in request.session:
        return redirect('/main')
    context = {
        'trip': Trip.objects.get(id=destination_id)
    }
    return render(request, 'belt_exam/destination.html', context)

def addTrip(request):
    if 'user' not in request.session:
        return redirect('/main')
    return render(request, 'belt_exam/add_trip.html')

def processTrip(request):
    if request.method == "POST":
        errors = Trip.objects.validateRequest(request.POST)
        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
            return redirect('/travels/add')
        startDate = datetime.strptime(request.POST['fromDate'], "%b %d, %Y").strftime("%Y-%m-%d")
        endDate = datetime.strptime(request.POST['toDate'], "%b %d, %Y").strftime("%Y-%m-%d")
        newTrip = Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], fromDate=startDate, toDate=endDate, creator_id=request.session['user'])
        newTrip.save()
    return redirect('/travels')

def processJoin(request, trip_id):
    trips = Trip.objects.filter(id=trip_id)
    if len(trips) == 1:
        trip = trips[0]
        trip.joined_users.add(getUser(request))
    return redirect('/travels')

def getUser(request):
    return User.objects.get(id=request.session['user'])

def deleteTrip(request, trip_id):
    trips = Trip.objects.filter(id=trip_id)
    if len(trips) == 1:
        trip = trips[0]
        trip.delete()
    return redirect('/travels')

def unjoinTrip(request, trip_id):
    trips = Trip.objects.filter(id=trip_id)
    if len(trips) == 1:
        trip = trips[0]
        trip.joined_users.remove(getUser(request))
        trip.save()
    return redirect('/travels')
