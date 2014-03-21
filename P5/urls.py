from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',

#    url(r'^admin/', include(admin.site.urls)),

    url(r'^home', 'static_pages.views.home', name='home'),
#    url('^help', 'static_pages.views.help', name='help'),
#    url('^about', 'static_pages.views.about', name='about'),

)


