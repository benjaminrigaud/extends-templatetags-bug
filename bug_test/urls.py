from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import MyView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', MyView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
