from django.db import models
from django.contrib.auth.models import User
     
class UserFoodPrefs(models.Model):

	class Meta: 
		app_label = 'recipemonkeyapp'

	likes=models.ManyToManyField('GroceryItem',null=True,related_name='food_likes')
	dislikes=models.ManyToManyField('GroceryItem',null=True,related_name='food_dislikes')
	user = models.ForeignKey(User, unique=True)