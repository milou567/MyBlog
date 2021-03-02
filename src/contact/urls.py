from django.urls import path

from . import views

urlpatterns = [
    path("", views.MyContactListView.as_view(), name="my_contact"),
    path("newsletter/", views.NewsletterView.as_view(), name="newsletter"),
]
