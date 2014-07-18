from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^all/$', 'poems.views.poems'),
	url(r'^social_poem/$', 'poems.views.social_poem'),
	url(r'^get/(?P<poem_id>\d+)/$', 'poems.views.poem'),
	url(r'^create/$', 'poems.views.create'),
	url(r'^like/(?P<poem_id>\d+)/$', 'poems.views.like_poem'),
	url(r'^comment/(?P<poem_id>\d+)/$', 'poems.views.comment'),
	
    url(r'^admin/', include(admin.site.urls)),
)
