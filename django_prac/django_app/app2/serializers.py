from rest_framework import serializers
from .models import Movie, Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class ReviewSeralizer(serializers.ModelSerializer):
    movie_name = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = "__all__"
        # exclude = ["movie"]
    def get_movie_name(self, object):
        return object.movie.name

class MovieReviewSeralizer(serializers.ModelSerializer):
    movie_name = serializers.SerializerMethodField()
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ["movie"]
    def get_movie_name(self, object):
        return object.movie.name