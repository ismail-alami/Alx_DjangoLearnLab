from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Review
from .serializers import UserSerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UserProfile(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        # Add user's reviews to the response
        reviews = Review.objects.filter(user=user)
        review_serializer = ReviewSerializer(reviews, many=True)
        data = serializer.data
        data['reviews'] = review_serializer.data
        return Response(data)

class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['movie_title']
    filterset_fields = ['rating']
    ordering_fields = ['rating', 'created_date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.method in ['PUT', 'DELETE']:
            return Review.objects.filter(user=self.request.user)
        return Review.objects.all()

class MovieReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['rating', 'created_date']
    filterset_fields = ['rating']

    def get_queryset(self):
        movie_title = self.kwargs['movie_title']
        return Review.objects.filter(movie_title__icontains=movie_title)