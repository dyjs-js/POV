import requests
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import GptPhoto
from .serializers import GptPhotoSerializer


class GPTPhotoDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return GptPhoto.objects.get(pk=pk)
        except GptPhoto.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        gptPhoto = self.get_object(pk)
        serializer = GptPhotoSerializer(
            gptPhoto,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        gptPhoto = self.get_object(pk)
        if gptPhoto.user != request.user:
            raise PermissionDenied
        serializer = GptPhotoSerializer(
            gptPhoto,
            data=request.data,
            partial=True,  # 일부만 수정 가능
        )
        if serializer.is_valid():
            updated_gptPhoto = serializer.save()
            serializer = GptPhotoSerializer(
                updated_gptPhoto,
                context={"request": request},
            )
            return Response(
                serializer.data,
            )
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        gptPhoto = self.get_object(pk)
        if (gptPhoto.book and gptPhoto.book.user != request.user) or (
            gptPhoto.movie and gptPhoto.movie.user != request.user
        ):
            raise PermissionDenied
        gptPhoto.delete()
        return Response(status=HTTP_200_OK)


class GetUploadGPTURL(APIView):
    def post(self, request):
        url = f" https://api.cloudflare.com/client/v4/accounts/{settings.CF_ID}/images/v2/direct_upload"
        one_time_url = requests.post(
            url, headers={"Authorization": f"Bearer {settings.CF_TOKEN}"}
        )
        one_time_url = one_time_url.json()
        result = one_time_url.get("result")
        return Response({"uploadURL": result.get("uploadURL")})
