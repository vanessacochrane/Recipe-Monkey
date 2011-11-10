from django.db import models
from recipemonkeyapp.utils.unitconversion import convertToGrams
class RecipeIngredient(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'

	
	quantity=models.FloatField()
	quantityMeasure=models.CharField(max_length=256,null=True,blank=True)  #probably should be a choice or separate object
	processing=models.CharField(max_length=256,null=True,blank=True)  #probably should be a choice or separate object
	keyIngredientFlag=models.NullBooleanField()
	item=models.ForeignKey('groceryItem')
	
	recipe=models.ForeignKey('Recipe')

	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s-%s " % (self.item.name,self.recipe.name) 
		

	@property
	def quantityInGrams(self):
		
		q=self.quantity
		m=self.quantityMeasure
		
		if m == '':
			return q*self.item.unitweight
			
		else:
			return convertToGrams(q,m)
			
	@property
	def cost(self):
		
		q=self.quantityInGrams
		
		price=self.item.latestUnitPriceGrams
		
		
		
		return q*price
		
		
	
