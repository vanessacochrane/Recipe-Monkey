from django.db import models
from django.contrib.auth.models import User
     
class UserFoodPrefs(models.Model):

	class Meta: 
		app_label = 'recipemonkeyapp'

	likes=models.ManyToManyField('GroceryItem',null=True,blank=True,related_name='food_likes')
	dislikes=models.ManyToManyField('GroceryItem',null=True,blank=True,related_name='food_dislikes')
	user = models.ForeignKey(User, unique=True)
	
	
	def checkRecipeDislikes(self,recipe):
		"""
		Checks food preferences versus a recipe
		
		"""
				
		for i in recipe.ingredients.all():
			for l in self.dislikes.all():
				if i==l:
					return True
					
		return False
					
	def checkRecipeLikes(self,recipe):
		"""
		Checks food preferences versus a recipe

		"""

		for i in recipe.ingredients.all():
			for l in self.likes.all():
				if i==l:
					return True

		return False
		
	def recipeInXLastEaten(self,recipe,x):
		"""
		Checks if recipe was eaten in the last x meals

		"""
		
		eaten=self.user.planner_set.all().order_by('-date')[:x]
		
		for e in eaten:
			if len(e.recipes.filter(id=recipe.id))>0:
				return True
		
		
		return False
		
		
	