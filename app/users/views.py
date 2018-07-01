from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return render(request, 'auth/login.html')


def sign_up(request):
    return render(request, 'auth/sign-up.html')


def authentication(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if action == 'login':
            user = authenticate(username=username, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse('products:index'))
        elif action == 'register':
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect(reverse('users:login'))
        else:
            pass
    else:
        return redirect(reverse('users:login'))
