from django.urls import path
from .views import GoalListView, GoalCreateView, GoalDetailView, GoalUpdateView, GoalDeleteView, GoalListCreateAPIView, GoalRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('goals/list/', GoalListView.as_view(), name='goal-list'),
    path('goals/create/', GoalCreateView.as_view(), name='goal-create'),
    path('goals/<int:pk>/detail/', GoalDetailView.as_view(), name='goal-detail'),
    path('goals/<int:pk>/update/', GoalUpdateView.as_view(), name='goal-update'),
    path('goals/<int:pk>/delete/', GoalDeleteView.as_view(), name='goal-delete'),

    path('api/v1/goals/', GoalListCreateAPIView.as_view(), name='goal-list-create-api-view'),
    path('api/v1/goals/<int:pk>/', GoalRetrieveUpdateDestroyAPIView.as_view(), name='goal-detail-api-view'),

]
