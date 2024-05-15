import requests
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import GptPhoto


class GPTPhotoDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return GptPhoto.objects.get(pk=pk)
        except GptPhoto.DoesNotExist:
            raise NotFound

    def delete(self, request, pk):
        GptPhoto = self.get_object(pk)
        if (GptPhoto.book and GptPhoto.book.user != request.user) or (
            GptPhoto.movie and GptPhoto.movie.user != request.user
        ):
            raise PermissionDenied
        GptPhoto.delete()
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
