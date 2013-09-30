from django.conf.urls import patterns, url
from django.views.generic import TemplateView

#from ribbit import views

urlpatterns = patterns('',

                        url(r'^$', 'ribbit.views.index'), # root
                        url(r'^login$', 'ribbit.views.login_view'), # login
                        url(r'^logout$', 'ribbit.views.logout_view'), # logout
                        url(r'^signup$', 'ribbit.views.signup'), # signup
                        url(r'^ribbits$', 'ribbit.views.public'), # public ribbits
                        url(r'^submit$', 'ribbit.views.submit'), # submit new ribbit
)

