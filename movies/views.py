from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT

from .models import Movie
from .serializers import MovieSerializer

# Create your views here.


class Movies(APIView):
    def get(self, request):
        all_movies = Movie.objects.all()
        serializer = MovieSerializer(
            all_movies,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            new_movie = serializer.save()
            return Response(
                MovieSerializer(new_movie).data,
            )
        else:
            return Response(serializer.errors)


class MovieDetail(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(
            movie,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_movie = serializer.save()
            return Response(
                MovieSerializer(updated_movie).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=HTTP_204_NO_CONTENT)
