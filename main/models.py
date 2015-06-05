from django.db import models
from django.contrib.auth.models import User



class Spare(models.Model):
	name = models.CharField(max_length=150)
	price = models.CharField(max_length=100)
	count = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.name


class Lube(models.Model):
	name = models.CharField(max_length=150)
	price = models.CharField(max_length=100)
	count = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.name


class Npn(models.Model):
	name = models.CharField(max_length=150)
	price = models.CharField(max_length=100)
	count = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.name


class Attender(models.Model):
	name = models.CharField(max_length=150)
	phone = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name


class Service(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name


class Job(models.Model):

   	name = models.CharField(max_length=100)
	address = models.TextField()
	attendee = models.ForeignKey(Attender)
	model_no = models.CharField(max_length=100)
	registration_no = models.CharField(max_length=200)
	date = models.DateTimeField(default=None, blank=True)
	service_type = models.ForeignKey(Service)

	def __unicode__(self):
		return self.name

class Manager(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=150)

	def __unicode__(self):
		return self.name
