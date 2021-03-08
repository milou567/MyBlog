from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Newsletter, AddOrder


class NewsletterForm(forms.ModelForm):
    """Форма подписки по email"""
    captcha = ReCaptchaField()

    class Meta:
        model = Newsletter
        fields = ("email", "captcha")
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Подпишись на новости, введи email..."})
        }
        labels = {
            "email": ''
        }


class OrderForm(forms.ModelForm):
    """Форма принятия заказа"""

    class Meta:
        model = AddOrder
        fields = ("name", "email", "website", "country", "text")