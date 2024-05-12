from django.db import models
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
