from rest_framework import serializers
from .models import Book
from users.serializers import TinyUserSerializer
from medias.serializers import PhotoSerializer
from liked.models import Liked


class BookListSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    is_liked_count = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            "pk",
            "title",
            "author",
            "review_title",
            "is_owner",
            "is_liked",
            "is_liked_count",
            "photos",
            "is_public",
        )

    def get_is_owner(self, book):
        request = self.context["request"]
        if request:
            return book.user == request.user
        return False

    def get_is_liked(self, book):
        request = self.context["request"]
        if request:
            if request.user.is_authenticated:
                return Liked.objects.filter(
                    user=request.user,
                    book__pk=book.pk,
                ).exists()
        return False

    def get_is_liked_count(self, book):
        return Liked.objects.filter(
            book__pk=book.pk,
        ).count()


class BookDetailSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    is_liked_count = serializers.SerializerMethodField()

    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        # 모든 필드를 보여줌
        fields = "__all__"

    def get_is_owner(self, book):
        request = self.context["request"]
        if request:
            return book.user == request.user
        return False

    def get_is_liked(self, book):
        request = self.context["request"]
        if request:
            if request.user.is_authenticated:
                return Liked.objects.filter(
                    user=request.user,
                    book__pk=book.pk,
                ).exists()
        return False

    def get_is_liked_count(self, book):
        return Liked.objects.filter(
            book__pk=book.pk,
        ).count()
