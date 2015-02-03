from django.views import generic
from django.http import HttpResponse
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from posts import models


def hello_fn(request, name="World"):
    return HttpResponse("Hello {}!".format(name))


class HelloView(View):

    def get(self, request, name="World"):
        return HttpResponse("Hello {}!".format(name))


class GreetView(View):
    greeting = "Hello {}!"
    default_name = "World"

    def get(self, request, **kwargs):
        name = kwargs.pop("name", self.default_name)
        return HttpResponse(self.greeting.format(name))


class SuperVillainView(GreetView):
    greeting = "We are the future, {}. Not them. "
    default_name = "my friend"


class FeedMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feed"] = models.Post.objects.viewable_posts(
            self.request.user)
        return context


class LoginRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class MyFeed(LoginRequiredMixin, FeedMixin, generic.CreateView):
    model = models.Post
    template_name = "myfeed.html"
    success_url = reverse_lazy("my_feed")


# from braces.views import StaticContextMixin


# class CtxView(StaticContextMixin, generic.TemplateView):
#     template_name = "ctx.html"
#     static_context = {"latest_profile": Profile.objects.latest('pk')}
