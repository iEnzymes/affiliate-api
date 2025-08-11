from rest_framework import generics

from core.models import Product, Room, Category, Tag
from core.utils import get_product_filters
from .serializers import ProductSerializerList, ProductSerializerDetailed


class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializerList

    def get_queryset(self):
        filters = get_product_filters(self.request.query_params)
        return Product.objects.filter(**filters)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializerDetailed

    queryset = Product.objects.all()