import datetime
from haystack.indexes import *
from haystack import site
from recipemonkeyapp.models import Recipe,GroceryItem


class RecipeIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    tags = CharField()
    tag_list = MultiValueField()
    url = CharField(indexed=False)
    season_start=CharField()
    
    def prepare_tags(self, obj):
        return ' '.join([tag.name for tag in obj.tags.all()])
        
    def prepare_season_start(self,obj):
        
        if obj.seasonStart is None:
            return 'no season'
        else:
            return obj.seasonStart.strftime('%B')
            
        
     
        
    def prepare_tag_list(self, obj):
        return [tag.name for tag in obj.tags.all()]
            
    def prepare_url(self, obj):
        return obj.get_absolute_url()

class GroceryItemIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    tags = CharField()
    tag_list = MultiValueField()
    url = CharField(indexed=False)
    season_start=CharField()
    
    def prepare_tags(self, obj):
        return ' '.join([tag.name for tag in obj.tags.all()])
        
    def prepare_season_start(self,obj):
        
        if obj.seasonStart is None:
            return 'no season'
        else:
            return obj.seasonStart.strftime('%B')
        
        
    def prepare_tag_list(self, obj):
        return [tag.name for tag in obj.tags.all()]
            
    def prepare_url(self, obj):
        return obj.get_absolute_url()

site.register(Recipe, RecipeIndex)
site.register(GroceryItem, GroceryItemIndex)
