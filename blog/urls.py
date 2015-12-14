from django.conf.urls import url
from blog.views import about, article

__author__ = 'Pritok'

urlpatterns = [
    url(r'^about/$', about, name="about"),
    url(r'^(?P<slug>[-\w]+)$', article, name="article"),
]
