from django.db import models

class Store(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
		
	name=models.CharField(max_length=256)
	storeType=models.CharField(max_length=256)
