from django.db import models

from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
	# model.CharField is variables of field
	# question_text/pub_dte is the field's name,it's table field's name
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	


	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	# bug fixed for TestCase
	# def was_published_recently(self):
	# 	now = timezone.now()
	# 	return now - datetime.timedelta(days=1) <= self.pub_date <= now

	def __str__(self):
		return self.question_text


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text