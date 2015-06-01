from django.db import models
from django.contrib.auth.models import User



class Job(models.Model):
	name = models.CharField(max_length=100)
	address = models.TextField()
	attendee = models.ForeignKey(User)
	model_no = models.CharField(max_length=100)
	registration_no = models.CharField(max_length=200)


	def __unicode__(self):
		return self.name
