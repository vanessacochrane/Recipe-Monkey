from django.db import models
from recipemonkeyapp.models.instruction import Instruction
from datetime import datetime

class SubRecipe(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
	
	
	mainRecipe=models.ForeignKey('Recipe',related_name='parent')
	recipe=models.ForeignKey('Recipe',related_name='subrecipe')
	
	quantity=models.FloatField()
	
	optional=models.BooleanField(default=False)