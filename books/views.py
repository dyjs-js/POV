from django.conf import settings
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.exceptions import (
    NotFound,
    PermissionDenied,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookListSerializer, BookDetailSerializer
from liked.serializers import LikedSerializer
from medias.serializers import PhotoSerializer


class Books(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_books = Book.objects.all()
        serializer = BookListSerializer(
            all_books,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = BookDetailSerializer(
            data=request.data,
            context={"request": request},
        )
        if serializer.is_valid():
            new_book = serializer.save()
            serializer = BookDetailSerializer(new_book)
            return Response(
                serializer.data,
            )
        else:
            return Response(serializer.errors)


class BookDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookDetailSerializer(
            book,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        if book.user != request.user:
            raise PermissionDenied
        serializer = BookDetailSerializer(
            book,
            data=request.data,
            partial=True,  # 일부만 수정 가능
        )
        if serializer.is_valid():
            updated_book = serializer.save()
            serializer = BookDetailSerializer(
                updated_book,
                context={"request": request},
            )
            return Response(
                serializer.data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        book = self.get_object(pk)
        if book.user != request.user:
            raise PermissionDenied
        book.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class BookLiked(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        book = self.get_object(pk)
        serializer = LikedSerializer(
            book.liked.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        user = request.user
        book = self.get_object(pk)
        existing_like = book.liked.filter(user=user).first()
        if existing_like:
            existing_like.delete()
            return Response(
                {"message": "Your like has been removed."},
                status=HTTP_204_NO_CONTENT,
            )

        serializer = LikedSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
                book=self.get_object(pk),
            )
            serializer = LikedSerializer(review)
            return Response(serializer.data)


class BookPhotos(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        book = self.get_object(pk)
        if request.user != book.user:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(book=book)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
