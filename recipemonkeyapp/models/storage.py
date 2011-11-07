from django.db import models
from django.contrib.contenttypes import generic

class Storage(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
	
	
	name=models.CharField(max_length=256)
	items = generic.GenericRelation('StorageItem',related_name='storedItem')
	#url....
	
	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.name) 


