from django.db import models

class PlannerMeal(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'

	recipe=models.ForeignKey('Recipe')
	planner=models.ForeignKey('Planner')
	course=models.CharField(max_length=256)