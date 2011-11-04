from django.contrib import admin

from recipemonkeyapp.models import *

class RecipeAdmin(admin.ModelAdmin):
	""" Object to control the behaviour of the linked object in the Admin interface
	"""
	list_display = ['id','name']
	list_filter = ['name']
	ordering = []
	search_fields = ['name']

class InstructionAdmin(admin.ModelAdmin):
	""" Object to control the behaviour of the linked object in the Admin interface
	"""
	list_display = ['order','recipe','step']
	ordering = ['order']

admin.site.register(Recipe,RecipeAdmin)	
admin.site.register(Instruction,InstructionAdmin)	
	






	
