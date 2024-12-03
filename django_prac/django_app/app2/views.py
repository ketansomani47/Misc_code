from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .serializers import MovieSerializer, ReviewSeralizer
from .models import Movie, Review
from .serializers import MovieReviewSeralizer
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import CustomPagination

class MovieListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MovieDetailsAPIView(generics.RetrieveUpdateDestroyAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ReviewListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSeralizer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['movie__name']
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['movie__name']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ReviewDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSeralizer

class MovieReviewAPIView(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = MovieReviewSeralizer

    def get_queryset(self):
        print(self.kwargs)
        pk = self.kwargs['pk']
        return Review.objects.filter(movie = pk)

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = Movie.objects.get(pk=pk)
        serializer.save(movie=movie)
