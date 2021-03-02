from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from .models import Newsletter
from .forms import NewsletterForm

from articles.models import Article


class MyContactListView(ListView):
    """Список публикаций"""

    model = Article
    template_name = "contact/contact.html"
    # ordering = "title" #сортировка публикаций
    # context_object_name = "articles"


class NewsletterView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = "/"
