from rest_framework import serializers
from .models import Book
from users.serializers import TinyUserSerializer


class BookListSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Book
        # 모든 필드를 보여줌
        fields = (
            "pk",
            "title",
            "author",
            "review_title",
            "is_owner",
        )

    def get_is_owner(self, book):
        request = self.context["request"]
        return book.user == request.user


class BookDetailSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Book
        # 모든 필드를 보여줌
        fields = "__all__"

    def get_is_owner(self, book):
        request = self.context["request"]
        return book.user == request.user
