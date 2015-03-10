from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import SignInAndSignUp, LogoutView, AboutView
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', SignInAndSignUp.as_view(template_name='home.html'),
        name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^myabout/$', TemplateView.as_view(template_name='myabout.html'),
        name='myabout'),
    url(r'^accounts/logout$', LogoutView.as_view(),
        name='logout'),

    url(r'^active/1/$',
        TemplateView.as_view(template_name="customtags.html"),
        name="active1"),
    url(r'^active/2/$',
        TemplateView.as_view(template_name="customtags.html"),
        name="active2"),
    url(r'^active/3/$',
        TemplateView.as_view(template_name="customtags.html"),
        name="active3"),
    
    url(r'^admin/', include(admin.site.urls)),
)
