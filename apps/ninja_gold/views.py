from django.shortcuts import render, redirect
from random import randint

# Create your views here.
def index(request):
    if 'actions' not in request.session:
        request.session['actions'] = []
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'ninja_gold/index.html')

def process_money(request, id):
    index = int(id)
    if index == 0:
        amount = randint(10, 20)
        request.session['gold'] += amount
        request.session['actions'].append("You got " + str(amount))
    if index == 1:
        amount = randint(5, 10)
        request.session['gold'] += amount
        request.session['actions'].append("You got " + str(amount))
    if index == 2:
        amount = randint(2, 5)
        request.session['gold'] += amount
        request.session['actions'].append("You got " + str(amount))
    if index == 3:
        amount = randint(-50, 50)
        request.session['gold'] += amount
        request.session['actions'].append("You got " + str(amount))
    return redirect('/')
