from django.conf.urls import url
from qa.views import test, question, questions_list, popular

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
	url(r'^$', test, name='questions_list'),
	url(r'^login/$', test, name='login'),
	url(r'^signup/$', test, name='signup'),
	url(r'^ask/.*$', "qa.test", name='ask'),
	url(r'^new/.*$', "test", name='new'),

	url(r'^\?page=(?P<page>\d+)', questions_list, name='questions_list'),	 	
	url(r'^popular/', popular, name='popular'),
	#url(r'^popular/\?page=(?P<page>\d+)', popular, name='popular'),
	url(r'^question/(?P<pk>\d+)/$', question, name='question'),

]