from django.urls import path
from .views import MovieListAPIView, MovieDetailsAPIView, ReviewListAPIView, ReviewDetailsAPIView
from .views import MovieReviewAPIView
urlpatterns = [
    path('movie_list/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailsAPIView.as_view(), name='movie_detail'),
    path('review_list/', ReviewListAPIView.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetailsAPIView.as_view(), name='review_detail'),
    path('movie/<int:pk>/review/', MovieReviewAPIView.as_view(), name='movie_review'),
]