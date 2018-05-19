from django.shortcuts import render
from random import randint

# Create your views here.
def index(request):
    if not ('attempts' in request.session):
        request.session["attempts"] = 1
    else:
        request.session["attempts"] += 1
    out = ""
    for i in range(0, 15):
        if (randint(0, 10) < 5):
            out += str(chr(randint(0, 26) + ord('A')))
        else:
            out += str(randint(0, 9))
    context = {
        'random_word': out,
        'attempts': request.session["attempts"]
    }
    return render(request, 'random_word/index.html', context)
