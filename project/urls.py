from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^poems/', include('poems.urls')),

	# user auth urls 
    url(r'^accounts/login/$','clouds.views.login'),
    url(r'^accounts/auth/$','clouds.views.auth_views'),
    url(r'^accounts/logout/$','clouds.views.logout'),
    url(r'^accounts/loggedin/$','clouds.views.loggedin'),
    url(r'^accounts/invalid/$','clouds.views.invalid_login'),
    url(r'^accounts/register/$','clouds.views.register_user'),
    url(r'^accounts/register_success/$','clouds.views.register_success'),

    url(r'^admin/', include(admin.site.urls)),
)
