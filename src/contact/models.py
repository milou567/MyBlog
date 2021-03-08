from django.db import models
from django.contrib.auth.models import User


class Newsletter(models.Model):
    """Подписка по email"""

    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class AddOrder(models.Model):
    """Добавление заказов"""

    name = models.CharField("Имя", max_length=100)
    email = models.EmailField()
    website = models.CharField("Веб-сайт", max_length=150)
    country = models.CharField("Страна", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"