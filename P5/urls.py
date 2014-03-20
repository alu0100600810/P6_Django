from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',

#    url(r'^admin/', include(admin.site.urls)),


    url('^home', 'static_pages.views.home', name='home'),
#    url('^help', 'static_pages.views.help', name='help'),
#    url('^about', 'static_pages.views.about', name='about'),

)

