from django.db import models

class Instruction(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'

	#guid=models.CharField(max_length=32,primary_key=True)
	order=models.IntegerField()
	step=models.CharField(max_length=2048)
	
	#account_type=models.CharField(max_length=2048)
	recipe=models.ForeignKey('Recipe')

	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.step) 
