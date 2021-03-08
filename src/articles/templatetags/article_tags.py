from django import template
from articles.models import Article


register = template.Library()

@register.inclusion_tag('articles/tags/last_article.html')
def get_last_article(count=4):
    article = Article.objects.order_by("id")[:count]
    return {"last_article": article}