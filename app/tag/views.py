from rest_framework import generics

from core.models import Tag
from core.utils import get_basic_filters
from .serializers import TagSerializer

class TagListView(generics.ListCreateAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
      filters = get_basic_filters(self.request.query_params)

      return Tag.objects.filter(**filters)

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()