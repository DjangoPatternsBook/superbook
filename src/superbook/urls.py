from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import SignInAndSignUp, LogoutView, AboutView
from chapter07 import views


urlpatterns = patterns(
    '',
    url(r'^$', SignInAndSignUp.as_view(template_name='home.html'),
        name='home'),
    url(r'^about/$', AboutView.as_view(),
        name='about'),
    url(r'^accounts/logout$', LogoutView.as_view(),
        name='logout'),

    url(r'^forms/$',
        views.FormView.as_view(),
        name="forms"),

    url(r'^cbv-form/$',
        views.ClassBasedFormView.as_view(),
        name="cbv-form"),

    url(r'^gfv-form/$',
        views.GenericFormView.as_view(),
        name="gfv-form"),


    url(r'^newsletter-form/$',
        views.NewsletterView.as_view(),
        name="newsletter-form"),

    url(r'^admin/', include(admin.site.urls)),
)
