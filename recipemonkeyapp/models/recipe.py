from django.db import models
from recipemonkeyapp.models.instruction import Instruction
from recipemonkeyapp.models.storageitem import StorageItem
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from taggit.managers import TaggableManager

class Recipe(models.Model):
    """
    An object to represent a Recipe.
    """

    class Meta:
        app_label = 'recipemonkeyapp'

    #: the name of the recipe
    name=models.CharField(max_length=256)
    #: fk for the cuisine of the recipe eg: Indian
    cuisine=models.ForeignKey('Cuisine',null=True,blank=True)
    #: the course of the recipe eg: Main, Dessert
    course=models.CharField(max_length=256,null=True,blank=True)
    #: the number of servings produced by the recipe
    serving=models.IntegerField(null=True,blank=True)
    #: the measure used for servings eg: people
    servingMeasure=models.CharField(max_length=256,null=True,blank=True)
    #: fk for the source of the recipe eg: Jamie's Italian
    source=models.ForeignKey('Source',null=True,blank=True)
    #: note for the recipe eg: substitute x for y
    note=models.TextField(null=True,blank=True)
    #: image of the recipe
    photo=models.ImageField(upload_to='recipephotos',null=True,blank=True)
    #: many to many fk for the recipe ingredients (through the RecipeIngredient object)
    ingredients = models.ManyToManyField('GroceryItem', through='RecipeIngredient')
    #: many to many fk for the recipe instructions
    instructions = models.ManyToManyField('Instruction',related_name='steps')
    #: flag to indicate whether the recipe is seasonal (determined by key ingredients)
    seasonal = models.BooleanField(default=False)
    #: many to many fk for subrecipes linked to this recipe (through the SubRecipe object)
    subrecipes = models.ManyToManyField('Recipe',related_name='subRecipes',through='SubRecipe',null=True,blank=True)
    #: taggit object for the assignment of tags
    tags = TaggableManager()


    @models.permalink
    def get_absolute_url(self):
        """
        Returns the django detailed view url for this object
        """
        return ('recipemonkeyapp.views.recipe.detail', [str(self.id)])

    def __unicode__(self):
        """ Returns the custom output string for this object
        """
        return "%s" % (self.name)

    def season(self):
        """
        Searches key ingredients to determine the seasonality of this recipe
        """

        kis=self.recipeingredient_set.filter(keyIngredientFlag=True)

        startDate=None
        endDate=None

        for ki in kis:
            iSeasonStart=ki.item.seasonStart
            iSeasonEnd=ki.item.seasonEnd

            if iSeasonStart is None or iSeasonEnd is None or not ki.item.seasonal:
                continue

            if startDate is None:
                startDate=iSeasonStart

            if endDate is None:
                endDate=iSeasonEnd

            if startDate < iSeasonStart:
                startDate = iSeasonStart

            if endDate > iSeasonEnd:
                endDate = iSeasonEnd


        return (startDate,endDate)

    @property
    def seasonEnd(self):
        """
        The end month of the recipe's season
        """

        return self.season()[1]

    @property
    def storeditems(self):
        """
        Returns a list of StorageItems in which this recipe is stored
        """
        mytype=ContentType.objects.get_for_model(self)
        stored=StorageItem.objects.filter(content_type=mytype,object_id=self.id).order_by('date_added')
        return stored

    @property
    def inSeason(self):
        """
        Flag to indicate whether this recipe is currently in season
        """

        if not self.seasonal:
            return True

        today=datetime.today().date()

        if self.seasonStart is None or self.seasonEnd is None:
            return False

        if self.seasonEnd<self.seasonStart:
            if today.month>=self.seasonStart.month or today.month<=self.seasonEnd.month:
                return True
            else:
                return False
        else:
            if today.month>=self.seasonStart.month and today.month<=self.seasonEnd.month:
                return True
            else:
                return False




    @property
    def seasonStart(self):
        """
        The start month of this recipe's season
        """

        return self.season()[0]

    @property
    def cost(self):
        """
        The cost of this recipe (derived from ingredient costs)
        """

        c=0
        for r in self.recipeingredient_set.all():
            c+=r.cost

        return round(c,2)

    @property
    def costPerServe(self):
        """
        The cost per serve found as total cost / number of servings
        """

        if self.serving == 0 or self.serving is None:
            return 0



        return round(self.cost / self.serving,2)
