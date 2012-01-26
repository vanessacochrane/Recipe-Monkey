from django.db import models
from django.contrib.contenttypes import generic
from recipemonkeyapp.models.storageitem import StorageItem
from django.contrib.contenttypes.models import ContentType

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
		
		
	@property
	def storeditems(self):
	    
	    mytype=ContentType.objects.get_for_model(self)
	    stored=StorageItem.objects.filter(content_type=mytype,object_id=self.id).order_by('date_added')
	    return stored




