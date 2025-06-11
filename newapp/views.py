from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Welcome to the New App!</h1><p>This is the index page of the new app.</p>')
    
