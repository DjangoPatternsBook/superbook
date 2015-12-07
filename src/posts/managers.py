from django.db.models.query import QuerySet
from django.db.models import Q


class PostQuerySet(QuerySet):
    def public_posts(self):
        return self.filter(privacy="public")

    def private_posts(self, user):
        """ Includes only posts sent by user or marked user as reciepient"""
        return self.filter(Q(privacy="individual"),
                           Q(posted_by=user) | Q(recipient=user))

    def viewable_posts(self, user):
        combined = self.public_posts() | self.private_posts(user)
        return combined.order_by("-created")

PostManager = PostQuerySet.as_manager
