from rest_framework import serializers
from .models import Movie
from users.serializers import TinyUserSerializer


class MovieListSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            "pk",
            "review_title",
            "title",
            "director",
            "is_owner",
        )

    def get_is_owner(self, book):
        request = self.context["request"]
        return book.user == request.user


class MovieDetailSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_is_owner(self, book):
        request = self.context["request"]
        return book.user == request.user
