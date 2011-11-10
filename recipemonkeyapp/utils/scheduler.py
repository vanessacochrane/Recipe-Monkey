
from recipemonkeyapp.models import Recipe,Planner,PlannerMeal
from django.contrib.auth.models import User

import calendar
from datetime import datetime
import random

def test_schedule():
	
	startDate=datetime(2011,11,1)
	
	p=User.objects.get(username='evandavey')
	people=[(p,),
			(p,),
			(p,),
			(p,),
			(p,),
			(p,),
			(p,),
		]
		
	weekNum=2
	

	schedule_meals(startDate,weekNum,people)

def schedule_meals(startDate,weekNum,people,maxMealRepeat=5):
	"""
	people=array of tuples for each day in week
	
	"""
	
	
	c=calendar.Calendar()
	
	week=c.monthdatescalendar(startDate.year, startDate.month)[weekNum-1]
	plan={}
	
	#get recipes that are in season
	breakfastRecipes=[x for x in Recipe.objects.filter(course='Breakfast') if True]
	
	from django.db.models import Q
	
	lunchRecipes=[x for x in Recipe.objects.filter(Q(course='Lunch')|Q(course='Soup')) if True]
	seasonalRecipes = [x for x in Recipe.objects.filter(course='Main') if x.inSeason]
	#seasonalRecipes = [x for x in Recipe.objects.all() if True]
	
	for r in seasonalRecipes:
		
		for mealp in people:
			
			r.likeWeight=0
			r.dislikeWeight=0
			r.inXLastEaten=0
			
			for p in mealp:
				prefs=p.userfoodprefs_set.all()[0]
				numpeople=len(mealp)
				if prefs.checkRecipeDislikes(r):
					#print "%s dislikes %s" % (p.username,r.name)
					r.dislikeWeight+=(1/numpeople)
				
				if prefs.checkRecipeLikes(r):
					#print "%s likes %s" % (p.username,r.name)
					r.likeWeight+=(1/numpeople)
				
				if prefs.recipeInXLastEaten(r,maxMealRepeat):
					#print "%s has eaten %s in last %d meals" % (p.username,r.name,maxMealRepeat)
					r.inXLastEaten+=1
				
			#print "%s has like weight of %f and dislike weight of %f and was in %d last eaten for %d people" % (r.name,r.likeWeight,r.dislikeWeight,maxMealRepeat,r.inXLastEaten)

		if r.inXLastEaten>0 and r.dislikeWeight>0:
			print "%s was rejected" % r.name
			seasonalRecipes.remove(r)

	
		
	if len(seasonalRecipes)<7:

		print 'insufficient recipes left for scheduling'
		return False
		
	picked={}
	i=0
	for dt in week:
		
		try:
			plan=Planner.objects.get(date=dt)
		except:
			plan=Planner()
			plan.date=dt
			plan.save()
		
		plan.users=people[i]
		plan.save()
		
		breakfast=random.choice(breakfastRecipes)
		lunch=random.choice(lunchRecipes)
		dinner=random.choice(seasonalRecipes)
	
		
		picked[dt]={'breakfast':breakfast,'secondary':lunch,'main':dinner}
		
		plan.recipes.clear() #delete old recipes
		
		m1=PlannerMeal(recipe=dinner,course='main',planner=plan)
		m1.save()
		
		m2=PlannerMeal(recipe=breakfast,course='breakfast',planner=plan)
		m2.save()
		
		m3=PlannerMeal(recipe=lunch,course='secondary',planner=plan)
		m3.save()
	
		seasonalRecipes.remove(dinner)
		
		
		
		
		i+=1
		
	print picked
	
	
	
	
	
	


