from rest_framework import generics
from rest_framework.response import Response

from core.models import Product, Category, Tag
from core.utils import get_product_filters
from .serializers import ProductSerializerList, ProductSerializerDetailed, ProductListFilteredResponseSerializer

class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductListFilteredResponseSerializer

    def get_queryset(self):
        filters = get_product_filters(self.request.query_params)
        return Product.objects.filter(**filters)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        products_data = ProductSerializerList(queryset, many=True, context={'request': request}).data

        return Response(products_data)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializerDetailed

    queryset = Product.objects.all()