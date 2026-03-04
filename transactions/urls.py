from django.urls import path
from .views import TransactionListView, TransactionCreateView, TransactionDetailView, TransactionUpdateView, TransactionDeleteView, TransactionListCreateAPIView, TransactionRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('transactions/list/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/create/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transaction/<int:pk>/detail/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactions/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction-update'),
    path('transactions/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction-delete'),

    path('api/v1/transactions/', TransactionListCreateAPIView.as_view(), name='transaction-list-create-api-view'),
    path('api/v1/transactions/<int:pk>/', TransactionRetrieveUpdateDestroyAPIView.as_view(), name='transaction-detail-api-view'),

]
