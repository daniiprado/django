from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm


# Create your views here.

def index(request):
    return render(request, 'products/index.html')


def products(request):
    data = serializers.serialize("json", Product.objects.order_by('id'))
    return HttpResponse(data, content_type='application/json', status=200)


def create(request):
    template = loader.get_template('products/create.html')
    form = ProductForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


def show(request, id):
    product = get_object_or_404(Product, pk=id)
    template = loader.get_template('products/show.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))