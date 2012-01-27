import datetime
from haystack.indexes import *
from haystack import site
from recipemonkeyapp.models import Recipe,GroceryItem


class RecipeIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)

class GroceryItemIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)

site.register(Recipe, RecipeIndex)
site.register(GroceryItem, GroceryItemIndex)
