from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
# from django.contrib import admin
from views import home, meet, tour, music, news, contact, get_tour_dates

urlpatterns = patterns('',
    # Examples:
     url(r'^$', home),
     url(r'^meet/', meet),
     url(r'^tour/', tour),
     # Grab the tour date coordinates in JSON
     url(r'^get_tour_dates/', get_tour_dates),
     url(r'^music/', music),
     url(r'^news/', news),
     url(r'^contact/', contact),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
