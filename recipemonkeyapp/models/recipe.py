from django.db import models
from recipemonkeyapp.models.instruction import Instruction
from datetime import datetime

class Recipe(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
	
	
	name=models.CharField(max_length=256)
	cuisine=models.ForeignKey('Cuisine',null=True,blank=True)
	course=models.CharField(max_length=256,null=True,blank=True)
	serving=models.IntegerField(null=True,blank=True)
	servingMeasure=models.CharField(max_length=256,null=True,blank=True)
	source=models.ForeignKey('Source',null=True,blank=True)
	note=models.TextField(null=True,blank=True)
	photo=models.ImageField(upload_to='recipephotos',null=True,blank=True)
 	ingredients = models.ManyToManyField('GroceryItem', through='RecipeIngredient')
	instructions = models.ManyToManyField('Instruction',related_name='steps')
	
	subrecipes = models.ManyToManyField('Recipe',related_name='subRecipes',through='SubRecipe',null=True,blank=True)
	
	
	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.name) 

	def season(self):
		
		kis=self.recipeingredient_set.filter(keyIngredientFlag=True)
		
		startDate=None
		endDate=None
		
		for ki in kis:
		
			
			iSeasonStart=ki.item.seasonStart
			iSeasonEnd=ki.item.seasonEnd
		
			if iSeasonStart is None or iSeasonEnd is None or not ki.item.seasonal:
				continue
			
			if startDate is None:
				startDate=iSeasonStart
			
			if endDate is None:
				endDate=iSeasonEnd
				
			if startDate < iSeasonStart:
				startDate = iSeasonStart
			
			if endDate > iSeasonEnd:
				endDate = iSeasonEnd
				
				
		return (startDate,endDate)
	
	@property
	def seasonEnd(self):

		return self.season()[1]


	@property
	def inSeason(self):
		
		
	
		today=datetime.today().date()

		if self.seasonStart is None or self.seasonEnd is None:
			return False

		if self.seasonEnd<self.seasonStart:
			if today.month>=self.seasonStart.month or today.month<=self.seasonEnd.month:
				return True
			else:
				return False
		else:
			if today.month>=self.seasonStart.month and today.month<=self.seasonEnd.month:
				return True
			else:
				return False
		

	

	@property
	def seasonStart(self):
		
		return self.season()[0]
		
	@property
	def cost(self):
		
		c=0
		for r in self.recipeingredient_set.all():
			c+=r.cost
			
		return round(c,2)
		
	@property
	def costPerServe(self):
		
		if self.serving == 0 or self.serving is None:
			return 0
			
		
		
		return round(self.cost / self.serving,2)	 
		
		