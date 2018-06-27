from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('json', views.products, name='products'),
    path('create', views.create, name='create'),
    path('store', views.store, name='store'),
    path('<int:id>', views.show, name='show'),
]