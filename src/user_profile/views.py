from django.contrib.auth.models import User
from articles.models import Article
from user_profile.models import Profile


from django.views.generic import DetailView, DeleteView, UpdateView


class UserDetailView(DetailView):
    model = User
    template_name = "user/profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "user"

    # def get_context_data(self, **kwargs):
    #     context = super(UserDetailView, self).get_context_data(**kwargs)
    #     context['articles'] = Article.objects.filter(author=context['user'])
    #     print(context)
    #     return context