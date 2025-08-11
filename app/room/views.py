from rest_framework import generics

from core.models import Room
from core.utils import get_basic_filters
from .serializers import RoomSerializer


class RoomListView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
      filters = get_basic_filters(self.request.query_params)

      return Room.objects.filter(**filters)

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.all()