from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    path('', RedirectView.as_view(url='/dashboard/', permanent=False)),

    path('dashboard/', include('dashboard.urls')),
    path('', include('categories.urls')),
    path('', include('goals.urls')),
    path('', include('transactions.urls')),

    path('api/v1/', include('authentication.urls')),
]
