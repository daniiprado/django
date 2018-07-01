from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    path('', auth_views.login, {'template_name': 'auth/login.html'}, name='login'),
    path('logout', auth_views.logout, {'next_page': 'users:login'}, name='logout'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('authenticate', views.authentication, name='authenticate'),
]
