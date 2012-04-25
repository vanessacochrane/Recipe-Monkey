import re

from piston.handler import BaseHandler
from piston.utils import rc, throttle
from recipemonkeyapp.models import Recipe


class RecipeHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'DELETE')
    fields = ('id', 'name','cusines','photo',('source', ('name',)),)
    #exclude = (re.compile(r'^private_'))
    model = Recipe


    def read(self, request, recipe_id=None):
       
        base = Recipe.objects

        if recipe_id:
            return base.get(pk=recipe_id)
        else:
            return base.all() # Or base.filter(...)
     
    @throttle(5, 10*60) # allow 5 times in 10 minutes
    def update(self, request, recipe_id):
        recipe = Recipe.objects.get(pk=recipe_id)

        recipe.name = request.PUT.get('name')
        recipe.save()

        return recipe

    def delete(self, request, recipe_id):
        recipe = Recipe.objects.get(pk=recipe_id)

        #if not request.user == post.author:
        #    return rc.FORBIDDEN # returns HTTP 401

        recipe.delete()

        return rc.DELETED # returns HTTP 204 return base.all() # Or base.filter(...)