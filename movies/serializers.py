from rest_framework import serializers
from .models import Movie
from users.serializers import TinyUserSerializer
from medias.serializers import PhotoSerializer
from liked.models import Liked


class MovieListSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "pk",
            "review_title",
            "title",
            "director",
            "is_owner",
            "is_liked",
            "photos",
        )

    def get_is_owner(self, movie):
        request = self.context["request"]
        return movie.user == request.user

    def get_is_liked(self, movie):
        request = self.context["request"]
        return Liked.objects.filter(
            user=request.user,
            movie__pk=movie.pk,
        ).exists()


class MovieDetailSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def get_is_owner(self, movie):
        request = self.context["request"]
        return movie.user == request.user

    def get_is_liked(self, movie):
        request = self.context["request"]
        return Liked.objects.filter(
            user=request.user,
            movie__pk=movie.pk,
        ).exists()
