from django.db import models

class Source(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
	
	
	name=models.CharField(max_length=256)
	
	#url....
	
	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.name) 


	