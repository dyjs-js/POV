from rest_framework.serializers import ModelSerializer
from .models import Liked
from users.serializers import TinyUserSerializer


class LikedSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Liked
        fields = (
            "payload",
            "user",
        )
