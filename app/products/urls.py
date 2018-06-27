from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('json', views.products, name='products'),
    path('create', views.create, name='create'),
    path('<int:id>', views.show, name='show'),
]