from django.db import models
from django.conf import settings

from common.models import CommonModel


# Create your models here.
class GptPhoto(CommonModel):
    file = models.TextField()

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="gptphotos",
    )
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="gptphotos",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="gptphotos",
        null=True,
    )
