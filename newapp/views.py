from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    name = 'Richmond'
    return render(request, 'index.html', {'name': name})
    

def counter(request):
    text = request.POST['text']
    number_of_words = len(text.split())
    return render(request, 'counter.html', {'number': number_of_words})


