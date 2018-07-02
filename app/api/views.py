from rest_framework import generics
from .serializers import ProductSerializer
from products.models import Product
from django.shortcuts import get_object_or_404


# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        queryset = self.get_query_set()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj
