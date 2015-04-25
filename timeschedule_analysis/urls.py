from django.conf.urls import patterns, include, url
from timeschedule_analysis import views

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login',
        {'template_name': 'index.html'}, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register, name='register'),
    # url(r'^moocs/(?P<mooc_id>\d+)/$', views.mooc, name='mooc'),
    url(r'^get_all_bins/$', views.get_all_bins, name='get_all_bins'),
    url(r'^send_new_bin/$', views.send_new_bin, name='send_new_bin'),
)