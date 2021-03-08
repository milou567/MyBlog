from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic.base import View
from .models import Newsletter
from .forms import NewsletterForm, OrderForm

from articles.models import Article
from django.contrib.auth.models import User


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


class AddOrderView(View):
    """Заказы"""

    def post(self, request, username):
        print(request.POST)
        form = OrderForm(request.POST)
        user = User.objects.get(username=username)
        print(user)
        if form.is_valid():
            form.save(commit=False)
            form.author = user
            print(form.author)
            form.save()
        return redirect("/")