from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView, CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('categories/list/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/detail/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    path('api/v1/categories/', CategoryListCreateAPIView.as_view(), name='category-list-create-api-view'),
    path('api/v1/categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail-api-view'),
]
