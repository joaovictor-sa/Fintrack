from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, serializers
from .forms import GoalForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class GoalListView(LoginRequiredMixin, ListView):
    model = models.Goal
    template_name = 'goal_list.html'
    context_object_name = 'goals'
    paginate_by = 10

    def get_queryset(self):
        queryset = models.Goal.objects.filter(user=self.request.user)
        category = self.request.GET.get('category')

        if category:
            queryset = queryset.filter(category__name__icontains=category)

        return queryset


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = models.Goal
    form_class = GoalForm
    template_name = 'goal_create.html'
    success_url = reverse_lazy('goal-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GoalDetailView(LoginRequiredMixin, DetailView):
    model = models.Goal
    template_name = 'goal_detail.html'

    def get_queryset(self):
        return models.Goal.objects.filter(user=self.request.user)


class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Goal
    template_name = 'goal_update.html'
    form_class = GoalForm
    success_url = reverse_lazy('goal-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_queryset(self):
        return models.Goal.objects.filter(user=self.request.user)


class GoalDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Goal
    template_name = 'goal_delete.html'
    success_url = reverse_lazy('goal-list')

    def get_queryset(self):
        return models.Goal.objects.filter(user=self.request.user)


class GoalListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.GoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Goal.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.requst.user)


class GoalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.GoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Goal.objects.filter(user=self.request.user)
