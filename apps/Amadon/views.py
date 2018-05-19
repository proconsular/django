from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'sum' not in request.session:
        request.session['sum'] = 0
    return render(request, 'Amadon/index.html')

def buy(request):
    if request.method == "POST":
        request.session['amount'] = float(request.POST['price']) * float(request.POST['quantity'])
        request.session['sum'] += float(request.POST['price']) * float(request.POST['quantity'])
        request.session['count'] += int(request.POST['quantity'])
    return redirect('/checkout')

def checkout(request):
    return render(request, 'Amadon/checkout.html')
