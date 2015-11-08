from . import models


class FeedMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context["feed"] = models.Post.objects.viewable_posts(
                self.request.user)
        return context
