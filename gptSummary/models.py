from django.db import models
from django.conf import settings
from common.models import CommonModel

# Create your models here.
#     - pk
#     - user FK
#     - book FK
#     - movie FK
#     - summary_source (요약을 원하는 내용)
#     - summarized_text(gpt를 통해서 요약된 내용)
# --> 여기에서 요약을 생성해서 movie 혹은 book에서 출력할 예정
# - 이미지 생성


class GptSummaryModel(CommonModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="gptSummary",
    )
    book = models.ForeignKey(
        "books.Book",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="gptSummary",
    )
    movie = models.ForeignKey(
        "movies.Movie",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="gptSummary",
    )
    summary_source = models.TextField(
        null=True,
        blank=True,
    )
    summarized_text = models.TextField(
        null=True,
        blank=True,
    )
