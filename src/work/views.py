from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from articles.models import Article


class MyWorkListView(ListView):
    model = Article
    template_name = "work/work.html"
    # ordering = "title" #сортировка публикаций
    # context_object_name = "about"
