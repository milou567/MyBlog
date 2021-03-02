from django.db import models


class Newsletter(models.Model):
    """Подписка по email"""
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email