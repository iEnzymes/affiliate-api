from django.urls import path

from .views import SubCategoryListView, SubCategoryDetailView

urlpatterns = [
    path('subcategory/', SubCategoryListView.as_view(), name='subcategory-list'),
    path('subcategory/<int:pk>/', SubCategoryDetailView.as_view(), name='subcategory-detail'),
]