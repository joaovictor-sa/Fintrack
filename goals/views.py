from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models, serializers
from .forms import GoalForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class GoalListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Goal
    template_name = 'goal_list.html'
    context_object_name = 'goals'
    paginate_by = 10
    permission_required = 'goals.view_goal'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')

        if category:
            queryset = queryset.filter(category__name__icontains=category)

        return queryset
    
class GoalCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Goal
    form_class = GoalForm
    template_name = 'goal_create.html'
    success_url = reverse_lazy('goal-list')
    permission_required = 'goals.add_goal'


class GoalDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Goal
    template_name = 'goal_detail.html'
    permission_required = 'goals.view_goal'


class GoalUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Goal
    template_name = 'goal_update.html'
    form_class = GoalForm
    success_url = reverse_lazy('goal-list')
    permission_required = 'goals.change_goal'


class GoalDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Goal
    template_name = 'goal_delete.html'
    success_url = reverse_lazy('goal-list')
    permission_required = 'goals.delete_goal'


class GoalListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.GoalSerializer


class GoalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.GoalSerializer

