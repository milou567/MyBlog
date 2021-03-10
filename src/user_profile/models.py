from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    bith_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField("Аватар", upload_to="user_profile/")
    url = models.SlugField(max_length=130, null=True)

    def __str__(self):
        return f"{self.user} - {self.country[:30]}"

    # def get_absolute_url(self):
    #     return reverse("user-profile", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Профайл"
        verbose_name_plural = "Профайлы"