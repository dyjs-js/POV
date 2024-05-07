from django.db import models
from django.conf import settings
from common.models import CommonModel


# Create your models here.
class Movie(CommonModel):
    """Model Definition for movies"""

    review_title = models.CharField(
        max_length=100,
    )
    title = models.CharField(
        max_length=100,
    )
    director = models.CharField(
        max_length=100,
        blank=True,
    )
    cast = models.CharField(
        max_length=200,
        blank=True,
    )
    content = models.TextField()
    summary = models.TextField()
    image = models.ImageField(blank=True)
    is_public = models.BooleanField(
        verbose_name="is Public?",
        default=True,
        help_text="Does this reivew allow public?",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="movies",
        null=True,
    )

    def __str__(self):
        return self.review_title
