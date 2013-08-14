from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from wordconfuse import views

urlpatterns = patterns('', 

		url(r'^$',TemplateView.as_view(template_name="wordconfuse/index.html")),
		url(r'^get_words$', views.get_words, name= 'get_words'),
		url(r'^gameover$', views.gameover, name='gameover'),
		url(r'^new_hs$', views.new_hs, name='new_hs'),
        url(r'^hs$',views.hs,name='hs'),

		)

