from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.exceptions import (
    NotFound,
    PermissionDenied,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer
from liked.serializers import LikedSerializer
from medias.serializers import PhotoSerializer

# Create your views here.


class Movies(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_movies = Movie.objects.all()
        serializer = MovieListSerializer(
            all_movies,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieDetailSerializer(
            data=request.data,
            context={"request": request},
        )
        if serializer.is_valid():
            new_movie = serializer.save()
            serializer = MovieDetailSerializer(new_movie)
            return Response(
                serializer.data,
            )
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class MovieDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieDetailSerializer(
            movie,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        if movie.user != request.user:
            raise PermissionDenied
        serializer = MovieDetailSerializer(
            movie,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_movie = serializer.save()
            serializer = MovieDetailSerializer(
                updated_movie,
                context={"request": request},
            )
            return Response(
                serializer.data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        if movie.user != request.user:
            raise PermissionDenied
        movie.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class MovieLiked(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = 3
        start = (page - 1) * page_size
        end = start + page_size
        room = self.get_object(pk)
        serializer = LikedSerializer(
            room.liked.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        user = request.user
        movie = self.get_object(pk)
        existing_like = movie.liked.filter(user=user).first()
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
                movie=self.get_object(pk),
            )
            serializer = LikedSerializer(review)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class MoviePhotos(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        movie = self.get_object(pk)
        if request.user != movie.user:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(movie=movie)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
