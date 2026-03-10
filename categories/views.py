from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, serializers
from .forms import CategoryForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class CategoryListView(LoginRequiredMixin, ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10

    def get_queryset(self):
        queryset = models.Category.objects.filter(user=self.request.user)
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.Category
    form_class = CategoryForm
    template_name = 'category_create.html'
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.Category
    template_name = 'category_detail.html'

    def get_queryset(self):
        return models.Category.objects.filter(user=self.request.user)
    

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Category
    template_name = 'category_update.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category-list')

    def get_queryset(self):
        return models.Category.objects.filter(user=self.request.user)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category-list')

    def get_queryset(self):
        return models.Category.objects.filter(user=self.request.user)
    

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Category.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Category.objects.filter(user=self.request.user)
