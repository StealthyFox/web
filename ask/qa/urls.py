from django.conf.urls import url
from qa.views import test, question, questions_list, popular
from qa.views import question_ask, question_answer
from qa.views import user_signup, user_login
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
	url(r'^$', questions_list, name='questions_list'),
	url(r'^new/.*$', test, name='new'),
	
	
	#url(r'^logout/.*$', user_logout, name='new'),
	url(r'^login/$', user_login, name='login'),
	url(r'^signup/$', user_signup, name='signup'),
	url(r'^answer/', question_answer, name='question_answer'),
	url(r'^ask/', question_ask, name='question_ask'),
	url(r'^\?page=(?P<page>\d+)', questions_list, name='questions_list'),	 	
	url(r'^popular/', popular, name='popular'),
	url(r'^question/(?P<pk>\d+)/$', question, name='question'),

]
