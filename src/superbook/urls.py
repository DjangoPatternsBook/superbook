from django.conf.urls import patterns, include, url
from django.contrib import admin
from profiles.views import SignInAndSignUp, LogoutView, AboutView
from chapter04 import views

urlpatterns = patterns(
    '',
    url(r'^$', SignInAndSignUp.as_view(template_name='home.html'),
        name='home'),
    url(r'^about/$', AboutView.as_view(),
        name='about'),
    url(r'^accounts/logout$', LogoutView.as_view(),
        name='logout'),

    url(r'^admin/', include(admin.site.urls)),

    # Chapter 4 URLs
    # ----------------------
    url(r'^hello-fn/(?P<name>\w+)/$', views.hello_fn),
    url(r'^hello-fn/$', views.hello_fn),

    url(r'^hello-cl/(?P<name>\w+)/$', views.HelloView.as_view()),
    url(r'^hello-cl/$', views.HelloView.as_view()),

    url(r'^hello-su/(?P<name>\w+)/$', views.SuperVillainView.as_view()),
    url(r'^hello-su/$', views.SuperVillainView.as_view()),

    url(r'^myfeed/$', views.MyFeed.as_view()),
    url(r'^public/$', views.PublicPostJSONView.as_view())
)
