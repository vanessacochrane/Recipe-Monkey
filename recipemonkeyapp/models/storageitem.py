from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from recipemonkeyapp.models.storagelog import StorageLog

class StorageItem(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
		
	storage=models.ForeignKey('Storage')
	object_id = models.PositiveIntegerField(blank=True)
	content_object = generic.GenericForeignKey('content_type', 'object_id',blank=True)
	content_type = models.ForeignKey(ContentType,blank=True)
	quantity=models.FloatField()
	quantityMeasure=models.CharField(max_length=256)
	date_added=models.DateField(auto_now_add=True,null=True)
	barcode=models.CharField(max_length=256,blank=True,null=True)
	
	
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
				sl.dateAdded=old.date_added
				sl.save()
				
				if self.quantity <= 0:
				    old.delete()
				
		
		if self.quantity > 0:
		    super(StorageItem, self).save(*args, **kwargs) # Call the "real" save() method.