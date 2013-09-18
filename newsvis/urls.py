from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from newsvis import views

urlpatterns = patterns('',

#                        url(r'^save_json$',views.save_comment,name='save_comment'),
                       url(r'^$', TemplateView.as_view(template_name="newsvis/index.html")),
#                        url(r'^(?P<comment_id>\d+)/$', views.detail, name='detail'),
)

