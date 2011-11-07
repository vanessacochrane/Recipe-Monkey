from django.db import models
from recipemonkeyapp.models.storageitem import StorageItem
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

class GroceryItem(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'


	name=models.CharField(max_length=256)
	category=models.ForeignKey('GroceryCategory')
	seasonStart=models.DateField(null=True)  #how to make month only?
	seasonEnd=models.DateField(null=True)
	store=models.ForeignKey('Store',null=True)
	unitcost=models.FloatField(default=0)
	unitweight=models.FloatField(default=0)
	

	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.name)
		
		
	def storeditems(self):
		mytype=ContentType.objects.get_for_model(self)
		stored=StorageItem.objects.filter(content_type=mytype,object_id=self.id).order_by('date')

		return stored
		
	def quantity(self):
		
		stored=self.storeditems()
		
		q=0
		for s in stored:
			q+=s.quantity
			
		return q
		
	@property
	def inSeason(self):

	
		today=datetime.today().date()
		
		if self.seasonStart is None or self.seasonEnd is None:
			return False

		if today.month>=self.seasonStart.month and today.month<=self.seasonEnd.month:
			return True
		else:
			return False
	
	