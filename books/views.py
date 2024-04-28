from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    PermissionDenied,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Book
from .serializers import BookListSerializer, BookDetailSerializer


class Books(APIView):
    def get(self, request):
        all_books = Book.objects.all()
        serializer = BookListSerializer(
            all_books,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = BookDetailSerializer(
                data=request.data,
                context={"request": request},
            )
            if serializer.is_valid():
                new_book = serializer.save()
                return Response(
                    BookDetailSerializer(new_book).data,
                )
            else:
                return Response(serializer.errors)


class BookDetail(APIView):
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
        if not request.user.is_authenticated:
            raise NotAuthenticated
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
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if book.user != request.user:
            raise PermissionDenied
        book.delete()
        return Response(status=HTTP_204_NO_CONTENT)
