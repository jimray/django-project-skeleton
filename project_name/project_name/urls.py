from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # include urls from your app like so
    # url(r'^', include('my_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
