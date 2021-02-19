from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from articles.models import Article


class AboutListView(ListView):
    model = Article
    template_name = "about/about.html"
    # ordering = "title" #сортировка публикаций
    # context_object_name = "about"
