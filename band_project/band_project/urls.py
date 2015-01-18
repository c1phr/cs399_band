from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
# from django.contrib import admin
from views import home, meet

urlpatterns = patterns('',
    # Examples:
     url(r'^$', home, name='home'),
     url(r'^meet/', meet),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
