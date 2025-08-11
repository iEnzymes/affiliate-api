from django.urls import path

from .views import TagListView, TagDetailView

urlpatterns = [
    path('tag/', TagListView.as_view(), name='tag-list'),
    path('tag/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
]