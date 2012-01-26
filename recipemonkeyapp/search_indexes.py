import datetime
from haystack.indexes import *
from haystack import site
from recipemonkeyapp.models import Recipe


class RecipeIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)


site.register(Recipe, RecipeIndex)
