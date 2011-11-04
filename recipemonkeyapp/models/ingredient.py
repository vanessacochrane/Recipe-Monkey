from django.db import models

class Ingredient(models.Model):
	
	class Meta: 
		app_label = 'recipemonkeyapp'

	SEASON_CHOICES = (
       	('01','January'),
 		('02','February'),
 		('03','March'), 
		('04','April'),
		('05','May'), 
		('06','June'), 
		('07','July'),
		('08','August'),
		('09','September'),
		('10','October'),
		('11','November'),
		('12','December'),
		('98','N/A')
		('99','unknown')
	) 

	CATEGORY_CHOICES = (
       	('01','fruit & vegetable'),
 		('02','dairy & eggs'),
 		('03','meat & poultry'), 
		('04','fish & seafood'),
		('05','frozen'), 
		('06','fresh herbs'),
		('08','tins, jars & bottles'),
		('09','dried herbs & spices'),
		('10','sugar'),
		('11','pasta, rice & cereal'),
		('97','other'),
	)

	STORE_CHOICES = (
       	('01','supermarket'),
 		('02','butcher'),
 		('03','fishmonger'), 
		('04','speciality store'),
		('05','grocers'), 
		('97','other'),
	)

	#guid=models.CharField(max_length=32,primary_key=True)
	name=models.CharField(max_length=256)
	category=models.CharField(max_length=2, choices=CATEGORY_CHOICES)
	seasonStart=models.CharField(max_length=2, choices=SEASON_CHOICES)
	seasonEnd=models.CharField(max_length=2, choices=SEASON_CHOICES)
	store=models.CharField(max_length=2, choices=STORE_CHOICES)
	
	#account_type=models.CharField(max_length=2048)
	recipeIngredient=models.ForeignKey('RecipeIngredient')

	def __unicode__(self):
		""" Returns the custom output string for this object
		"""
		return "%s" % (self.name)