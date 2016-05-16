from django.db import models
from django.contrib.auth.models import User

class Question (models.Model):
	titile = models.CharField(max_length = 255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField()
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User)
	
	#class Meta:
		#db_table = 'questions'
		
class Answer (models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
	
	#class Meta:
		#db_table = 'answers'

