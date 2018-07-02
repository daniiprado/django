from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('products', views.ProductList.as_view(), name='index'),
]