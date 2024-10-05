from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'  

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile')
    
]