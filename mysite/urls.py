from django.conf.urls import patterns, include, url
from mysite.views import home,sites,summary,abcsite,xyzsite,summary_average,demosite

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^sites/$',sites),
    url(r'^summary/$',summary),
    url(r'^sites/1',demosite),
    url(r'^sites/2/$',abcsite),
    url(r'^sites/3/$',xyzsite),
    url(r'^summary_average/$',summary_average)
)
