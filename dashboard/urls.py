from django.urls import path
from .views import DashboardView, DashboardAPIView


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
]
