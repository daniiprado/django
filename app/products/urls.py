from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('json', views.products, name='products'),
    path('create', views.create, name='create'),
    path('store', views.store, name='store'),
    path('<int:id>', views.show, name='show'),
    # Class Base View
    path('class-base-view', views.ProductList.as_view(), name='index_c_b_v'),
    path('class-base-view/<int:id>', views.ProductDetail.as_view(), name='show_c_b_v'),
]