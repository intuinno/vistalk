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
     url(r'^comments/',include('django.contrib.comments.urls')),
     url(r'^movievis/',include('movievis.urls',namespace="movievis")),
     url(r'^yelpvis/',include('yelpvis.urls',namespace='yelpvis')),
     url(r'^ribbit/',include('ribbit.urls',namespace='ribbit')),
     url(r'^newsvis/',include('newsvis.urls',namespace='newsvis')),
     url(r'^newsvis2/',include('newsvis2.urls',namespace='newsvis2')),
     url(r'^todo/',include('todo.urls',namespace='todo')),
     url(r'', include('social_auth.urls')),


     # url(r'^$','blog.views.index'),
     # url(r'^(?P<slug>[\w\-]+)/$','blog.views.post'),
)
