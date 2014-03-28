from django.db import models
from django.db import models
from djangotoolbox.fields import ListField


class Resume(models.Model):
	"""
	Model to store resume details
	"""

	name = models.CharField(max_length=100)
	gender = models.CharField(max_length=5)
	experience = models.IntegerField()
	university = models.CharField(max_length=100)
	graduation_year = models.IntegerField()
	skills = ListField()

	def __unicode__(self):
		return self.name


	
		
