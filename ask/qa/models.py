from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Question (models.Model):
	title = models.CharField(max_length = 255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name="question_author")
	likes = models.ManyToManyField(User, related_name="question_like")
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('question', kwargs={'pk': self.pk})
	#class Meta:
		#db_table = 'questions'
		
class Answer (models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
	
	#class Meta:
		#db_table = 'answers'

