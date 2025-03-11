from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('', include('login.urls')),
    path('', include('register.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Add this line
]
