from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from base.views import SallesView


urlpatterns = patterns('',

                       url(r'^salle/(?P<regroupement>\w+)/$', SallesView.as_view(), name='liste_salle'),
)

