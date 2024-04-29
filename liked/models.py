from django.db import models
from django.conf import settings
from common.models import CommonModel

# Create your models here.


class Liked(CommonModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="liked",
    )
    payload = models.TextField(
        null=True,
        blank=True,
    )
    # 좋아요는 하나의 book 이나 movie를 가지고, book or movie는 여러개의 좋아요를 가질 수 있음
    book = models.ForeignKey(
        "books.Book",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="liked",
    )
    movie = models.ForeignKey(
        "movies.Movie",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="liked",
    )

    # def __str__(self) -> str:
    #     return self.name
