from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, serializers
from .forms import TransactionForm


class TransactionListView(LoginRequiredMixin, ListView):
    model = models.Transaction
    template_name = 'transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 10


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = models.Transaction
    form_class = TransactionForm
    template_name = 'transaction_create.html'
    success_url = reverse_lazy('transaction-list')


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = models.Transaction
    template_name = 'transaction_detail.html'


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Transaction
    form_class = TransactionForm
    template_name = 'transaction_update.html'
    success_url = reverse_lazy('transaction-list')


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Transaction
    template_name = 'transaction_delete.html'
    success_url = reverse_lazy('transaction-list')


class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permission_classes = [IsAuthenticated]


class TransactionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permission_classes = [IsAuthenticated]
