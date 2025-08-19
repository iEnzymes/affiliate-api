from rest_framework import generics

from core.models import SubCategory
from core.utils import get_basic_filters
from .serializers import SubCategorySerializer


class SubCategoryListView(generics.ListCreateAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        filters = get_basic_filters(self.request.query_params)
        category_id = self.request.query_params.get('category_id')
        if category_id:
            filters['category'] = category_id
        return SubCategory.objects.filter(**filters)


class SubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        return SubCategory.objects.all()