from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="all_articles"),
    path(
        "articles/<slug:slug>/",
        views.ArticleDetailView.as_view(),
        name="detail_article",
    ),
    path("add-rating/", views.AddStarRating.as_view(), name="add_rating"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("search/", views.Search.as_view(), name="search"),
]
