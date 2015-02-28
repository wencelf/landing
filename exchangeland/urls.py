from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'landing.views.index', name='home'),
    url(r'^sendemail/$', 'landing.views.sendemail'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
