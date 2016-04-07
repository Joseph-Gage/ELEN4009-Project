from django.conf.urls import patterns, include, url
from friendAnalyzerApp.views import home

urlpatterns = patterns('',
    url(r'^$', 'friendAnalyzerApp.views.home'),
    url(r'^home/$', 'friendAnalyzerApp.views.home'),
    url(r'^friend-network/$', 'friendAnalyzerApp.views.friendNetwork'),
    url(r'^word-chart/$', 'friendAnalyzerApp.views.wordChart'),
    
)
