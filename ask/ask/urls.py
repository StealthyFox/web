from django.conf.urls import patterns, include, url
from qa.views import test, question, qa_list_all, qa_popular_all

from django.contrib import admin
admin.autodiscover()

#from qa.views import test

urlpatterns = patterns('',
	url(r'^$', test, name='home'),
	url(r'^login/$', test, name='login'),
	url(r'^signup/$', test, name='signup'),
	url(r'^ask/.*$', test, name='ask'),
	url(r'^new/.*$', test, name='new'),

	url(r'^\?page=(?P<page>\d+)', questions_list, name='questions_list'),	 	
	url(r'^popular/', popular, name='popular'),
	#url(r'^popular/\?page=(?P<page>\d+)', popular, name='popular'),
	url(r'^question/(?P<pk>\d+)/$', question, name='question'),

#url(r'^admin/', include(admin.site.urls)),
)
