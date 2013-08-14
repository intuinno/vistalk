from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:ddd
    # url(r'^$', 'vistalk3.views.home', name='home'),
    # url(r'^vistalk3/', include('vistalk3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

     url(r'^polls/',include('polls.urls',namespace="polls")),
     url(r'^wordconfuse/',include('wordconfuse.urls',namespace="wordconfuse")),
     url(r'^blog/',include('blog.urls',namespace="blog")),
     # url(r'^$','blog.views.index'),
     # url(r'^(?P<slug>[\w\-]+)/$','blog.views.post'),
)
