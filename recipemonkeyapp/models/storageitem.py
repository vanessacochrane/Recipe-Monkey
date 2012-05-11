from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from recipemonkeyapp.models.storagelog import StorageLog
import logging
from datetime import *

MEASURE_CHOICES = (
    ('SERVES', 'Serves'),
    ('G', 'Grams'),
)


class StorageItem(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
		
	storage=models.ForeignKey('Storage')
	object_id = models.PositiveIntegerField(blank=True,null=True)
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	content_type = models.ForeignKey(ContentType,blank=True,null=True)
	quantity=models.FloatField()
	quantityMeasure=models.CharField(max_length=256,choices=MEASURE_CHOICES)
	date_added=models.DateField(auto_now_add=True,null=True)
	barcode=models.CharField(max_length=256,blank=True,null=True)

	@property
	def expired(self):
	    
	    res=False
	    if expiry:
	        if self.expiry<date.today()
	            return True
	        
	    return res

	
	@property
	def near_expiry(self):
	    
	    res=False
	    if expiry and not self.expired:
	        if self.expiry-date.today()<timedelta(days=5)
	            return True
	        
	    return res
	
	@property
	def expiry(self):
	    
	    
	    try:
	        if self.storage.frozen:
	            m=self.content_object.expiryFrozenMultiplier
	        else:
	            m=1
	            
	        return self.date_added+timedelta(days=self.content_object.expiryDays*m)
	        
	    except:
	        logging.error('Error working out expiry')
	        return None
	
	
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