from django.db import models
from django.contrib.auth.models import User

class Planner(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
	
	
	date=models.DateField()
	users=models.ManyToManyField(User)
	recipes=models.ManyToManyField('Recipe')
	
	
	
	#url....
	
	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.date)
		
		
	def shopping(self):
		
		for r in self.recipes.all():
			for ri in r.recipeingredient_set.all():
				i=ri.item
				
				qdiff= i.quantity() - ri.quantity
				if qdiff < 0:
					print 'Need to buy %f of %s' % (abs(qdiff),i.name)
											
								