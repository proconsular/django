from django.shortcuts import render, redirect
import datetime

# Create your views here.
def index(request):

    if 'items' not in request.session:
        request.session['items'] = []

    return render(request, 'session_words/index.html')

def process(request):
    if request.method == "POST":
        item = {
            'word': request.POST['word'],
            'color': request.POST['color'],
            'date': str(datetime.datetime.now())
        }
        if 'big' in request.POST:
            item['big'] = True
        else:
            item['big'] = False
        request.session['items'] += [item]
    return redirect('/')

def clear(request):
    del request.session['items']
    return redirect('/')
