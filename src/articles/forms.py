from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Rating
from .models import RatingStar
from .models import Review


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""

    captcha = ReCaptchaField()

    class Meta:
        model = Review
        fields = ("name", "email", "text", "captcha")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Ваше имя..."}),
            "email": forms.EmailInput(attrs={"class": "form-control border", "placeholder": "Ваш email..."}),
            "text": forms.Textarea(attrs={"class": "form-control border", "placeholder": "Комментарий..."}),
        }


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""

    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)
