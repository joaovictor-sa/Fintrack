from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, serializers
from .forms import TransactionForm


class TransactionListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Transaction
    template_name = 'transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 10
    permission_required = 'transactions.view_transaction'


class TransactionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Transaction
    form_class = TransactionForm
    template_name = 'transaction_create.html'
    success_url = reverse_lazy('transaction-list')
    permission_required = 'transactions.add_transaction'


class TransactionDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Transaction
    template_name = 'transaction_detail.html'
    permission_required = 'transactions.view_transaction'


class TransactionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Transaction
    form_class = TransactionForm
    template_name = 'transaction_update.html'
    success_url = reverse_lazy('transaction-list')
    permission_required = 'transactions.change_transaction'

class TransactionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Transaction
    template_name = 'transaction_delete.html'
    success_url = reverse_lazy('transaction-list')
    permission_required = 'transactions.delete_transaction'    


class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permission_classes = [IsAuthenticated]


class TransactionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permission_classes = [IsAuthenticated]

