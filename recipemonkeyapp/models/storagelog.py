from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from datetime import datetime

class StorageLog(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
		
	storage=models.ForeignKey('Storage')
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	content_type = models.ForeignKey(ContentType)
	quantity=models.FloatField()
	dateAdded=models.DateField(null=True,blank=True)
	dateChanged=models.DateField(default=datetime.today)