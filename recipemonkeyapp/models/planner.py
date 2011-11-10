from django.db import models
from django.contrib.auth.models import User
import calendar
class Planner(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
	
	
	date=models.DateField()
	users=models.ManyToManyField(User)
	recipes=models.ManyToManyField('Recipe',through='PlannerMeal')
	
	#url....
	

	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.date)
		
		
	def shopping(self):
		
		for r in self.recipes.all():
			print "Meal: %s" % r.name 
			for ri in r.recipeingredient_set.all():
				i=ri.item
				
				qdiff= i.quantity() - ri.quantity
				if qdiff < 0:
					print '...need to buy %f%s of %s' % (abs(qdiff),ri.quantityMeasure,i.name)
											
	@property
	def breakfast(self):
		
		return self.plannermeal_set.get(course='breakfast').recipe.name				
		
	@property
	def dinner(self):

		return self.plannermeal_set.get(course='dinner').recipe.name				
	
	
	@property
	def lunch(self):

		return self.plannermeal_set.get(course='lunch').recipe.name				
	