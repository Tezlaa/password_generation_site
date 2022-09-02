from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, "generator/home.html")

def password(request):
    
    thepassword = ''
    
    characters = list('qwertyuiopasdfghjklzxcvbnm')
    
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list("~!@#$%^&*"))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    
    length = int(request.GET.get('length',12))
    
    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, "generator/password.html", {'password':thepassword})

def info(request):
    return render(request, "generator/info.html")