from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from todo import views

urlpatterns = patterns('',

                       url(r'^$','views.index'),
)

