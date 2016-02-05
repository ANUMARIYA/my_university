from django.conf.urls import patterns, include, url

from django.contrib import admin
from register.views import Home
admin.autodiscover()

urlpatterns = [

    url(r'^$',Home.as_view(), name='home'),
    # Examples:
    # url(r'^$', 'myuniversity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]