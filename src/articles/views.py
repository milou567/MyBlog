from django.shortcuts import redirect
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.base import View

from articles.models import Article

from .forms import ReviewForm


class ArticleListView(ListView):
    """Список публикаций"""

    model = Article
    queryset = Article.objects.filter(draft=False)
    template_name = "articles/index.html"
    ordering = "title"  # сортировка публикаций
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    """Полное описание публикаций"""

    model = Article
    template_name = "articles/article_detail.html"
    slug_field = "url"
    context_object_name = "article"


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        print(request.POST)
        form = ReviewForm(request.POST)
        article = Article.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.article = article
            form.save()
        return redirect(article.get_absolute_url())
