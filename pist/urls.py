from django.conf.urls import patterns, include, url
from conseptcar import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.sondageParticulierForm, name = "sondage1"),
    url(r'^home', views.sondageParticulierForm, name = "home"),



)
