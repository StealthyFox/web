from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Question (models.Model):
	title = models.CharField(max_length = 255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, default=1)
	likes = models.ManyToManyField(User, related_name="questions")
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
	author = models.ForeignKey(User, default=1)
	
	def __str__(self):
		return 'Answer by {}'.format(self.author)
	#class Meta:
		#db_table = 'answers'

