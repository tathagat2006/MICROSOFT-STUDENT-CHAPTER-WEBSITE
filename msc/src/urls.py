from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^team/$', views.team_page, name='team'),
    url(r'^gallery/$', views.main_gallery, name='gallery'),
    url(r'^newsfeed/$', views.newsfeed, name='newsfeed'),
    url(r'^newsfeed/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^events/msweek$', views.msweek_event, name='msweek'),
    url(r'^events/inspirus$', views.inspirus_event, name='inspirus'),
    url(r'^events/rumble$', views.rumble_event, name='rumble'),

    url(r'^contact/$', views.ContactView, name='contact'),

]