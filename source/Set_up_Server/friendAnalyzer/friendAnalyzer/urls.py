from django.conf.urls import patterns, include, url
from friendAnalyzerApp.views import home

urlpatterns = patterns('',
    url(r'^$', 'friendAnalyzerApp.views.home'),
    url(r'^home/$', 'friendAnalyzerApp.views.home'),
    
)
