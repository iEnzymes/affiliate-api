from rest_framework import generics

from core.models import Category
from core.utils import get_basic_filters
from .serializers import CategorySerializer

class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
      filters = get_basic_filters(self.request.query_params)

      return Category.objects.filter(**filters)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()