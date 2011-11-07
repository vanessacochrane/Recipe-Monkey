from django.db import models

class Cuisine(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
		
	name=models.CharField(max_length=256)
	parent = models.ForeignKey('self',blank=True,null=True,related_name='child')
	
	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.name)