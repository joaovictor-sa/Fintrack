from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, serializers
from .forms import TransactionForm


MONTHS = [
    (1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Março'), (4, 'Abril'),
    (5, 'Maio'), (6, 'Junho'), (7, 'Julho'), (8, 'Agosto'),
    (9, 'Setembro'), (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro'),
]


class TransactionListView(LoginRequiredMixin, ListView):
    model = models.Transaction
    template_name = 'transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 10

    def get_queryset(self):
        queryset = models.Transaction.objects.filter(user=self.request.user).order_by('-date')

        title = self.request.GET.get('title', '').strip()
        type_ = self.request.GET.get('type', '').strip()
        month = self.request.GET.get('month', '').strip()

        if title:
            queryset = queryset.filter(title__icontains=title)
        if type_ in ('income', 'expense'):
            queryset = queryset.filter(type=type_)
        if month.isdigit():
            queryset = queryset.filter(date__month=int(month))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['months'] = MONTHS
        return context


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = models.Transaction
    form_class = TransactionForm
    template_name = 'transaction_create.html'
    success_url = reverse_lazy('transaction-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = models.Transaction
    template_name = 'transaction_detail.html'

    def get_queryset(self):
        return models.Transaction.objects.filter(user=self.request.user)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Transaction
    form_class = TransactionForm
    template_name = 'transaction_update.html'
    success_url = reverse_lazy('transaction-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return models.Transaction.objects.filter(user=self.request.user)


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Transaction
    template_name = 'transaction_delete.html'
    success_url = reverse_lazy('transaction-list')

    def get_queryset(self):
        return models.Transaction.objects.filter(user=self.request.user)


class TransactionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # era self.requst (typo)


class TransactionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Transaction.objects.filter(user=self.request.user)
