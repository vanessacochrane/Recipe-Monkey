from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from recipemonkeyapp.models import Recipe,Instruction,RecipeIngredient


def index(request):
    	
	recipe_list=Recipe.objects.all()
	
	
		
	ct={'recipe_list':recipe_list,
	
	}
	
	return render_to_response('recipe/index.html',ct,context_instance=RequestContext(request))

def detail(request, recipe_id):
    
	try:
		r = Recipe.objects.get(pk=recipe_id)
	except Recipe.DoesNotExist:
		raise Http404

	instructions=Instruction.objects.filter(recipe=r).order_by('order')
	ingredients=RecipeIngredient.objects.filter(recipe=r)
	
	ct={'recipe':r,
		'ingredients':ingredients,
		'instructions':instructions,
	}
	
	return render_to_response('recipe/detail.html',ct,context_instance=RequestContext(request))