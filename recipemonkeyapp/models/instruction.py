from django.db import models

class Instruction(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'

	order=models.IntegerField(default=1)
	step=models.TextField()
	recipe=models.ForeignKey('Recipe')


	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.step) 
