from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def login(request):
    return render(request, 'auth/login.html')


def authentication(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
