from django.db import models
from django.conf import settings
from common.models import CommonModel


# Create your models here.
class GptPhoto(CommonModel):
    file = models.TextField()

    book = models.ForeignKey(
        "books.Book",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="gptPhotos",
    )
    movie = models.ForeignKey(
        "movies.Movie",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="gptPhotos",
    )
