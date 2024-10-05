from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import  PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, 
    CommentUpdateView, CommentDeleteView, post_detail


app_name = 'blog'  

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.postListView, name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]