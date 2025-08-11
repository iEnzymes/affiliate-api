from django.urls import path

from .views import RoomListView, RoomDetailView

urlpatterns = [
    path('room/', RoomListView.as_view(), name='room-list'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
]