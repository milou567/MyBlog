from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response

from .service import get_client_ip
from articles.models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer, ReviewCreateSerializer, CreateRatingSerializer


class ArticleListView(ListAPIView):
    """Вывод списка статей"""

    serializer_class = ArticleListSerializer
    filter_backends = (SearchFilter, OrderingFilter)

    def get_queryset(self):
        articles = Article.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
                   )
        return articles


class ArticleDetailView(APIView):
    """Вывод статьи"""
    def get(self, request, pk):
        article = Article.objects.get(id=pk, draft=False)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)


class ReviewCreateView(CreateAPIView):
    """Добавление отзыва к статье"""

    serializer_class = ReviewCreateSerializer



class AddStarRatingView(CreateAPIView):
    """Добавление рейтинга статье"""

    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))