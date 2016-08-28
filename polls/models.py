from django.db import models

# Create your models here.
class Question(models.Model):
	# model.CharField is variables of field
	# question_text/pub_dte is the field's name,it's table field's name
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text