from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views



urlpatterns = [

    path('article/', views.ArticleListView.as_view()),
    path('article/<int:pk>/', views.ArticleDetailView.as_view()),
    path('review/create/', views.ReviewCreateView.as_view()),
    path('rating/', views.AddStarRatingView.as_view()),
]