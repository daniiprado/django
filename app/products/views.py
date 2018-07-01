from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, get_object_or_404
# Class Base View
from django.views.generic import ListView, DetailView
# Mixins y Decorators
from django.contrib.auth.decorators import login_required
from products.mixins import LoginRequiredMixin


from .models import Product
from .forms import ProductForm


# Create your views here.

def index(request):
    return render(request, 'products/index.html')

@login_required()
def show(request, id):
    product = get_object_or_404(Product, pk=id)
    template = loader.get_template('products/show.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))


def products(request):
    data = serializers.serialize("json", Product.objects.order_by('id'))
    return HttpResponse(data, content_type='application/json', status=200)


@login_required()
def create(request):
    template = loader.get_template('products/create.html')
    form = ProductForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


@login_required()
def store(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            product.save()
            return HttpResponseRedirect(reverse('products:index'))
    else:
        return HttpResponseRedirect(reverse('products:index'))


# Class Base View


class ProductList(ListView):
    model = Product


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
