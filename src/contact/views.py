from django.http import HttpResponse
from django.shortcuts import redirect, render
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
    if User.username is not None:
        def post(self, request, username):
            print(request.POST)
            form = OrderForm(request.POST)
            user = User.objects.get(username=username)
        # if user is not None:
            print(user)
            if form.is_valid():
                form.save(commit=False)
                form.author = user
                print(form.author)
                form.save()
        # else:
        #     return render(request, 'accounts/login.html')
            return redirect("/")