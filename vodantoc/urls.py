from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from base.views import SallesView

admin.autodiscover()
from django.conf import settings


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'site_vo.views.home', name='home'),
                       # url(r'^site_vo/', include('site_vo.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:

                        url(r'^blog/', include('zinnia.urls')),
                       # Uncomment the next line to enable the admin:
                       #(r'^forum/account/', include('django_authopenid.urls')),
                       url(r'^calendar/', include('calendarium.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       # url(r'^admin_tools/', include('admin_tools.urls')),
                        url(r'^salles/', include('base.urls')),

                       url(r'^comments/', include('django_comments.urls')),

                       url(r'^', include('cms.urls')),




)

if settings.DEBUG:
    urlpatterns = patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')), ) + urlpatterns
