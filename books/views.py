import time
import os
from pathlib import Path
from openai import OpenAI
import environ
from django.conf import settings
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
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
from gptCreate.serializers import GptPhotoSerializer


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
        print(dir(request.user))
        serializer = BookDetailSerializer(
            data=request.data,
            context={"request": request},
        )
        if serializer.is_valid():
            new_book = serializer.save(user=request.user)
            serializer = BookDetailSerializer(
                new_book,
                context={"request": request},
            )
            return Response(
                serializer.data,
            )
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        time.sleep(1)  # ui 테스트를 위한 slepp
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
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

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
        # 이미 좋아요가 존재한다면 삭제
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
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


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
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# open ai api key 설정을 위한 세팅
env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
api_key = env("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


class BookGptPhotos(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound

    # pompt를 사용하여 이미지 생성 모델에 요청을 보내고, 응답으로 받은
    # 이미지 url을 반환
    def get_completion(self, prompt):
        query = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024",
        )
        response = query.data[0].url
        return response

    def post(self, request, pk):
        book = self.get_object(pk)
        if request.user != book.user:
            raise PermissionDenied

        prompt = f"{book.title}, {book.author}, context: {book.content}"
        file_url = self.get_completion(prompt)
        file_url = f"{file_url}"
        data = {"file": file_url}
        serializer = GptPhotoSerializer(data=data)
        if serializer.is_valid():
            gptphoto = serializer.save(book=book)
            serializer = GptPhotoSerializer(gptphoto)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
