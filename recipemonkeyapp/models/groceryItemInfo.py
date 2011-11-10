from django.db import models
from recipemonkeyapp.utils.tesco import Tesco

class GroceryItemInfo(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'


	date=models.DateField(auto_now=True)
	item=models.ForeignKey('GroceryItem')
	unitPrice=models.FloatField(default=0)
	unitType=models.CharField(max_length=256,null=True,blank=True)
	source=models.CharField(max_length=256)
	price=models.FloatField(default=0)
	
	@property
	def unitPriceGrams(self):
		
		p=self.unitPrice
		m=self.unitType
		
		if m=='100g':
			return p/100
		
		if m=='kg':
			return p/1000
		
		return p
		
	@property
	def priceGrams(self):

		p=self.price
		up=self.unitPrice
		m=self.unitType
		
		

		
		if m=='100g':
			if p==up:
				return p
				
			return p*10

		if m=='kg':
			return p*100

		return p