from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from recipemonkeyapp.models.storagelog import StorageLog

class StorageItem(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
		
	storage=models.ForeignKey('Storage')
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	content_type = models.ForeignKey(ContentType)
	quantity=models.FloatField()
	quantityMeasure=models.CharField(max_length=256)
	date=models.DateField()
	
	
	def loadold(self):
		
		try:
			return StorageItem.objects.get(pk=self.id)
		except:
			return None
	
	def save(self, *args, **kwargs):

	
		old=self.loadold()
		
	
		if old is not None:
			if old.quantity != self.quantity:
				sl=StorageLog()
				sl.storage=self.storage
				#sl.object_id=self.object_id
				#sl.content_type=ContentType.objects.get_for_model(self.content_object)
				sl.content_object=self.content_object
				sl.quantity=self.quantity-old.quantity
				sl.dateAdded=old.date
				sl.save()
				
				
		
		
		super(StorageItem, self).save(*args, **kwargs) # Call the "real" save() method.