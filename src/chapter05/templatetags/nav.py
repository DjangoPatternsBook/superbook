from django.core.urlresolvers import resolve
from django.template import Library

register = Library()


@register.simple_tag
def active_nav(request, url):
    url_name = resolve(request.path).url_name
    if url_name == url:
        return "active"
    return ""
