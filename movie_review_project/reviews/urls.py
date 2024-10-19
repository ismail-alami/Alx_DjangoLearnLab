from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UserRegister, 
    UserProfile,
    ReviewList, 
    ReviewDetail, 
    MovieReviewList
)

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('users/profile/', UserProfile.as_view(), name='user-profile'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('movies/<str:movie_title>/reviews/', MovieReviewList.as_view(), name='movie-reviews'),
]