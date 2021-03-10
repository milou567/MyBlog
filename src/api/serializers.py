from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import serializers
from articles.models import Article, Review, Rating
from user_profile.models import Profile



class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментарией, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ArticleListSerializer(serializers.ModelSerializer):
    """Список статей"""
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()
    class Meta:
        model = Article
        fields = ("id", "title", "author", "rating_user", "middle_star")


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("name", "text", "children")


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Полная статья"""

    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Article
        exclude = ("draft",)


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""

    class Meta:
        model = Rating
        exclude = ("star", "article")

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(ip=validated_data.get("ip", None), article=validated_data.get("article", None), defaults={"star": validated_data.get("star")})
        return rating