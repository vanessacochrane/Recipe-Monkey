from django.db import models
from recipemonkeyapp.models.storageitem import StorageItem
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

class GroceryItem(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'


	name=models.CharField(max_length=256)
	category=models.ForeignKey('GroceryCategory')
	seasonStart=models.DateField(null=True,blank=True)  #how to make month only?
	seasonEnd=models.DateField(null=True,blank=True)
	store=models.ForeignKey('Store',null=True,blank=True)
	tescoid=models.CharField(max_length=256)
	seasonal=models.BooleanField(default=False)
	EANBarcode=models.CharField(max_length=256,null=True,blank=True)
	
	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.name)
		
		
	
	def storeditems(self):
		mytype=ContentType.objects.get_for_model(self)
		stored=StorageItem.objects.filter(content_type=mytype,object_id=self.id).order_by('date')

		return stored
	
	@property	
	def quantity(self):
		
		stored=self.storeditems()
		
		q=0
		for s in stored:
			q+=s.quantity
			
		return q
	
	
	@property
	def unitweight(self):
		
		p=self.latestPriceGrams
		up=self.latestUnitPrice
		
		if up == 0:
			return 0
		
		return round(p/up,0)
	
	@property
	def latestPrice(self):

		gis=self.groceryiteminfo_set.all().order_by('date')[:1]

		if len(gis)==0:
			return 0

		return gis[0].price
	
	@property
	def latestPriceGrams(self):

		gis=self.groceryiteminfo_set.all().order_by('date')[:1]

		if len(gis)==0:
			return 0

		return gis[0].priceGrams
	
	@property
	def latestUnitPrice(self):
		
		gis=self.groceryiteminfo_set.all().order_by('date')[:1]
		
		if len(gis)==0:
			return 0
	
		return gis[0].unitPrice
	
	@property
	def latestUnitPriceGrams(self):
		
		gis=self.groceryiteminfo_set.all().order_by('date')[:1]

		if len(gis)==0:
			return 0

		return gis[0].unitPriceGrams
	
	@property
	def inSeason(self):

		if not self.seasonal:
			return True
	
		today=datetime.today().date()
		
		if self.seasonStart is None or self.seasonEnd is None:
			return False

		if today.month>=self.seasonStart.month and today.month<=self.seasonEnd.month:
			return True
		else:
			return False
	
	