from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from recipemonkeyapp.models import Recipe,Instruction,RecipeIngredient,StorageItem,SubRecipe


from django.http import HttpResponse
from elaphe import barcode 
from django.http import Http404

from recipemonkeyapp.forms import StorageItemForm
from django.forms.models import modelformset_factory
from django.contrib.contenttypes.models import ContentType

import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from django.contrib import messages

class RecipeTable(tables.Table):
    
    
    name = tables.LinkColumn('recipe_detail', args=[A('pk')])
    
    
    class Meta:
        model = Recipe
        exclude = ['id','photo','note','expiryDays','expiryFrozenMultiplier']
        attrs = {'class': 'table'}


def add_to_shopping(request,recipe_id):
    
    messages.error(request, 'Not Implemented: would add missing ingredients to shopping list') 
    
    return redirect(request.META.get('HTTP_REFERER','/'))
    
def cook(request,recipe_id):
    
    messages.add_message(request, messages.ERROR, 'Not Implemented: Yum yum, would use ingredients from storage and log') 

    return redirect(request.META.get('HTTP_REFERER','/'))


def index(request):
    
    table = RecipeTable(Recipe.objects.all())
    table.paginate(page=request.GET.get("page", 1))
    table.order_by = request.GET.get("sort")
    
    ct={'table':table,
    'recipes':Recipe.objects.all(),
    }
    
    return render_to_response('recipemonkey/recipe/index.html',ct,context_instance=RequestContext(request))

def detail(request, recipe_id):
    
	try:
		r = Recipe.objects.get(pk=recipe_id)
	except Recipe.DoesNotExist:
		raise Http404

	instructions=Instruction.objects.filter(recipe=r).order_by('order')
	ingredients=RecipeIngredient.objects.filter(recipe=r)
	subrecipes=SubRecipe.objects.filter(mainRecipe=r)
	
	ct={'recipe':r,
		'ingredients':ingredients,
		'instructions':instructions,
		'subrecipes':subrecipes,
	}
	
	return render_to_response('recipemonkey/recipe/detail.html',ct,context_instance=RequestContext(request))
	

def scan(request, id):

	try:
		i = Recipe.objects.get(pk=id)
	except Recipe.DoesNotExist:
		raise Http404

	StorageItemFormSet = modelformset_factory(StorageItem,fields=('storage','quantity'),max_num=2)	
	#StorageItemFormSet = modelformset_factory(StorageItem)


	if request.method == 'POST': # If the form has been submitted...

		formset =StorageItemFormSet(request.POST)

		if formset.is_valid():
			for form in formset:
				si=form.save(commit=False)
				
				
				si.content_object=i
				si.object_id=i.id
				si.content_type=ContentType.objects.get_for_model(i)
				    
				if si.quantity > 0:
				    si.save()
				        
				if si.quantity <=0:
				    if si.id:     
				        si.delete()

			return redirect('recipemonkeyapp.views.recipe.scan',id=i.id)

	else:

		formset =StorageItemFormSet(queryset=i.storeditems)

	ct={'recipe':i,
		'formset':formset,
	}


	return render_to_response('recipemonkey/recipe/detail.html',ct,context_instance=RequestContext(request))


def barcodeimg(request, id):

    try:
    	i = Recipe.objects.get(pk=id)
    except Recipe.DoesNotExist:
    	raise Http404

    response=HttpResponse(content_type='image/png')

    url="https://%s/recipemonkeyapp/recipe/scan/%s/" % ('recipemonkey.getoutsideandlive.com',i.id)

    img=barcode('qrcode',url,data_mode='8bits')

    img.save(response, 'PNG')

    return response