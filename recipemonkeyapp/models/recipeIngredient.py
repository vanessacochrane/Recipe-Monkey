from django.db import models

class recipeIngredient(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'

	name=models.CharField(max_length=256)
	quantity=models.IntegerField()
	quantityMeasure=models.CharField(max_length=256)
	processing=models.CharField(max_length=256)
	keyIngredientFlag=models.NullBooleanField()
	
	recipe=models.ForeignKey('Recipe')

	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.name)