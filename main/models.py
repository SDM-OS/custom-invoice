from django.db import models
from django.contrib.auth.models import User



class Spare(models.Model):
	name = models.CharField(max_length=150)
	price = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Attender(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=150)
	phone = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Job(models.Model):
	A = 0
	B = 1
	C = 2
	SERVICE_TYPE = (
		(A, "A"),
		(B, "B"),
		(C, "C"),
	)

   	name = models.CharField(max_length=100)
	address = models.TextField()
	attendee = models.ForeignKey(Attender)
	model_no = models.CharField(max_length=100)
	registration_no = models.CharField(max_length=200)
	start_date = models.DateTimeField(default=None, blank=True)
	end_date = models.DateTimeField(default=None, blank=True)
	service_type = models.PositiveIntegerField(choices=SERVICE_TYPE, default=A)

	def __unicode__(self):
		return self.name
