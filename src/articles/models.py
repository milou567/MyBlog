import datetime

from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    """Статьи"""

    title = models.CharField("название статьи", max_length=200)
    content = models.TextField("текст статьи")
    pub_date = models.DateTimeField("дата публикации", auto_now=True)
    art_image = models.ImageField("Изображение", upload_to="articles/")
    url = models.SlugField(max_length=130, null=True)
    draft = models.BooleanField("черновик", default=False)

    def __str__(self):
        return f"{self.title} - {self.content[:30]}"

    def was_publeshed_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    def get_absolute_url(self):
        return reverse("detail_article", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Review(models.Model):
    """Отзывы"""

    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        "self",
        verbose_name="Родитель",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    article = models.ForeignKey(
        Article, verbose_name="публикация", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} - {self.article}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
