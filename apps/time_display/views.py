from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    context = {
        'time': datetime.datetime.now()
    }
    return render(request, 'time_display/index.html', context)
