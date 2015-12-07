#!/usr/bin/env python
import os

SUPERUSER_NAME = "hexa"
SUPERUSER_PASSWORD = "hexa"
SUPERUSER_EMAIL = "hexa@superbook.com"

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superbook.settings")
    import django
    django.setup()
    print("Django configured...")
    from django.core import management
    print("Checking apps...")
    management.call_command('check')
    print("Migrating...")
    management.call_command('migrate', interactive=False, verbosity=2)

    # Create superuser
    print("Creating superuser...")
    from django.contrib.auth import get_user_model
    User = get_user_model()
    su = User.objects.create_superuser(username=SUPERUSER_NAME,
                                       email=SUPERUSER_EMAIL,
                                       password=SUPERUSER_PASSWORD)
    su.profile.bio = "An ex-KGB scientist who accidentally discovered human levitation"
    su.profile.save()
    su.first_name = "Hexa"
    su.save()
    print("""
    SUPERUSER CREATED!
    ------------------------

         NAME: {}
         PASSWORD: {}

    Login to the website with the above credentials.
    """.format(SUPERUSER_NAME, SUPERUSER_PASSWORD))

    #
    # Create another user
    blitz = User.objects.create_user(username="blitz",
                                     email="blitz@superbook.com",
                                     password="blitz")
    blitz.first_name = "Blitz"
    blitz.profile.bio = "A fine extra-terrestrial athlete"
    blitz.profile.save()
    blitz.save()

    #
    # Create fans
    fans = [User.objects.create_user(username="fan{}".format(i),
                                     email="fan{}@email.com".format(i),
                                     password="fan")
            for i in range(10)]

    #
    # Create some test posts
    from posts.models import Post
    Post.objects.create(posted_by=su, message="My first message")
    Post.objects.create(posted_by=su, message="My second message")
    Post.objects.create(posted_by=su, message="My third message")
    Post.objects.create(posted_by=blitz, message="Yo to Everyone!!!")
    Post.objects.create(posted_by=blitz,
                        privacy='individual',
                        recipient=blitz,
                        message="Yo to just Me...")
