from rest_framework.serializers import ModelSerializer
from .models import GptPhoto


class GptPhotoSerializer(ModelSerializer):

    class Meta:
        model = GptPhoto
        fields = "__all__"
