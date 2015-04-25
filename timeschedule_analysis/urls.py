from django.conf.urls import patterns, include, url
from timeschedule_analysis import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    # url(r'^moocs/(?P<mooc_id>\d+)/$', views.mooc, name='mooc'),
)