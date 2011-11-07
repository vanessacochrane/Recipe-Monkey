from django.contrib import admin

from recipemonkeyapp.models import *


class RecipeInstructionInline(admin.TabularInline):
	model = Instruction
	extra=0

class RecipeIngredientInline(admin.TabularInline):
	model = Recipe.ingredients.through


class RecipeAdmin(admin.ModelAdmin):
	""" Object to control the behaviour of the linked object in the Admin interface
	"""
	list_display = ['name','source','serving']
	list_filter = ['source','cuisine']
	ordering = []
	search_fields = ['name']
	inlines = [RecipeIngredientInline,RecipeInstructionInline]
	exclude=['instructions']
	
class GroceryItemAdmin(admin.ModelAdmin):
	list_display = ['name','category','seasonStart','seasonEnd','inSeason']
	list_filter = ['category','seasonStart']
	search_fields = ['name']

class RecipeIngredientAdmin(admin.ModelAdmin):
	""" Object to control the behaviour of the linked object in the Admin interface
	"""
	list_display = ['recipe','item','quantity','quantityMeasure','processing']
 	filter = ['recipe']

class InstructionAdmin(admin.ModelAdmin):
	""" Object to control the behaviour of the linked object in the Admin interface
	"""
	list_display = ['order','step']
	ordering = ['order']

class StorageItemAdmin(admin.ModelAdmin):
	""" Object to control the behaviour of the linked object in the Admin interface
	"""
	list_display = ['storage','content_object','quantity','date']
	ordering = ['date']
	
class StorageLogAdmin(admin.ModelAdmin):
	""" Object to control the behaviour of the linked object in the Admin interface
	"""
	list_display = ['dateChanged','storage','content_object','quantity','dateAdded']
	ordering = ['dateChanged']
	
class UserFoodPrefsAdmin(admin.ModelAdmin):
	""" Object to control the behaviour of the linked object in the Admin interface
	"""
	list_display = ['user']
	
class PlannerAdmin(admin.ModelAdmin):
	""" Object to control the behaviour of the linked object in the Admin interface
	"""
	list_display = ['date']

admin.site.register(Recipe,RecipeAdmin)	
admin.site.register(Instruction,InstructionAdmin)	
admin.site.register(RecipeIngredient,RecipeIngredientAdmin)	
admin.site.register(Store)	
admin.site.register(Source)	
admin.site.register(GroceryItem,GroceryItemAdmin)	
admin.site.register(GroceryCategory)	
admin.site.register(Cuisine)	
admin.site.register(Storage)	
admin.site.register(StorageItem,StorageItemAdmin)	
admin.site.register(StorageLog,StorageLogAdmin)	
admin.site.register(UserFoodPrefs,UserFoodPrefsAdmin)	
admin.site.register(Planner,PlannerAdmin)	







	
