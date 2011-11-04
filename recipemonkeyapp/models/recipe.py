from django.db import models
from recipemonkeyapp.models.instruction import Instruction

class Recipe(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'
	
	CUISINE_CHOICES = (
        (('Asian'), (
				('jap','Japanese'),
				('chi','Chinese'),
				('ind','Indian'),
				('tha','Thai'),
			)
		),
		('Mediterranean'), (
				('ita','Italian'),
				('gre','Greek'),
				('Middle Eastern')	
			)
		),
		('European'), (
				('French'),
				('German'),
			)
		),
		('Mexican'),
		('Russian'),
		('American'),
		('Australian'),
		('Unknown'),
	 )
		
	name=models.CharField(max_length=256)
	cuisine=models.CharField(max_length=256, choices=CUISINE_CHOICES)
	course=models.CharField(max_length=256)
	serving=models.IntegerField()
	servingMeasure=models.CharField(max_length=256)
	source=models.CharField(max_length=256)
	note=models.CharField(max_length=2048) 
	#photo=models.ImageField()

	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.name) 

	def list_steps(self):
		
		dqs=Instruction.objects.filter(recipe=self).order_by('order')
		
		for d in dqs:
			print d
		
		