from django.db import models
from django.conf import settings
from .managers import PostManager


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Postable(TimeStampedModel):
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
                                  null=True, related_name="%(class)ss")
    message = models.TextField(max_length=500)

    def __str__(self):
        return "{}: {:.30}".format(self.posted_by, self.message)

    class Meta:
        abstract = True
        ordering = ["-created"]


class Post(Postable):
    POST_PRIVACY = (
        ('public', 'Public'),
        ('individual', 'Individual')
    )
    privacy = models.CharField(max_length=12, choices=POST_PRIVACY,
                               default='public')
    # A recipient is needed if the privacy is set to "Individual"
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
                                  null=True, related_name="recieved_posts")
    objects = PostManager()


class Comment(Postable):
    parent_post = models.ForeignKey(Post)


class Like(models.Model):
    liked_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)

    def __str__(self):
        return "{} liked <{}>".format(self.liked_by, self.post)
