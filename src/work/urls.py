from django.urls import path

from . import views

urlpatterns = [
    path("", views.MyWorkListView.as_view(), name="my_work"),
]
