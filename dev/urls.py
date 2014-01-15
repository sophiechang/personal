from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
)

urlpatterns += patterns('',
    url(r'^$', 'content.views.home', name='index'),
    url(r'^contact/$', 'content.views.contact', name='contact'),
    url(r'^contact/thankyou/$', 'content.views.thankyou', name='thankyou'),
    url(r'^photospheres/tag/(?P<slug>[^\.]+)/$', 'content.views.view_tag', name='view_tag'),
    url(r'^photospheres/view/(?P<slug>[^\.]+)/$', 'content.views.view_photo', name='view_photo'),
    url(r'^photospheres/$', 'content.views.photospheres', name='photospheres'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}
    ))
