from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    return render(request, 'survey_form/index.html')

def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
    return redirect('/show')

def show(request):
    return render(request, 'survey_form/show.html')
