from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
# from django.contrib import admin
from views import home, meet, tour, music, news, contact
urlpatterns = patterns('',
    # Examples:
     url(r'^$', home),
     url(r'^meet/', meet),
     url(r'^tour/', tour),
     url(r'^music/', music),
     url(r'^news/', news),
     url(r'^contact/', contact),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
