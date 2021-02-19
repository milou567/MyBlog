from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from articles.models import Article


class MyContactListView(ListView):
    """Список публикаций"""

    model = Article
    template_name = "contact/contact.html"
    # ordering = "title" #сортировка публикаций
    # context_object_name = "articles"
