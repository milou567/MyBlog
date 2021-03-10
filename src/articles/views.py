from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.base import View

from articles.models import Article

from .forms import RatingForm
from .forms import ReviewForm
from .models import Rating


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        context["form"] = ReviewForm()
        return context


class AddStarRating(View):
    """Добавление рейтинга статье"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                article_id=int(request.POST.get("article")),
                defaults={"star_id": int(request.POST.get("star"))},
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        print(pk)
        form = ReviewForm(request.POST)
        article = Article.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.article = article
            form.save()
        return redirect(article.get_absolute_url())


class Search(ListView):
    """Поиск постов"""

    model = Article
    template_name = "articles/index.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(title__icontains=self.request.GET.get("q"))
