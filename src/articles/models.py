import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    """Статьи"""

    title = models.CharField("название статьи", max_length=200)
    content = models.TextField("текст статьи")
    quote = models.TextField("цитата", null=True)
    pub_date = models.DateTimeField("дата публикации", auto_now=True)
    art_image = models.ImageField("Изображение", upload_to="articles/")
    url = models.SlugField(max_length=130, null=True)
    draft = models.BooleanField("черновик", default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} - {self.content[:10]}"

    def was_publeshed_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    def get_absolute_url(self):
        return reverse("detail_article", kwargs={"slug": self.url})

    def get_review(self):
        return self.review_set.filter(parent__isnull=True)

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


class RatingStar(models.Model):
    """Звезда рейтинга"""

    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""

    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(
        RatingStar, on_delete=models.CASCADE, verbose_name="звезда"
    )
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="статья", related_name="ratings"
    )

    def __str__(self):
        return f"{self.star} - {self.article}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
