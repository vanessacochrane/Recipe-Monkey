from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from elaphe import barcode 
from recipemonkeyapp.models import GroceryItem,StorageItem
from django.contrib.sites.models import Site
from django.http import Http404
from recipemonkeyapp.forms import StorageItemForm
from django.forms.models import modelformset_factory
from django.contrib.contenttypes.models import ContentType
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from datetime import *

def labels(request):
	
	item_list=GroceryItem.objects.all()
	
	
		
	ct={'item_list':item_list,
	
	}
	
	return render_to_response('recipemonkey/groceryitem/labels.html',ct,context_instance=RequestContext(request))

   

class GroceryItemTable(tables.Table):
    
    name = tables.LinkColumn('groceryitem_detail', args=[A('pk')])
    
    class Meta:
        model = GroceryItem
        exclude = ['id','store','tescoName','tescoid','EANBarcode']
        

        
    def render_seasonStart(self, value):
        if value:
            return '%s' % value.strftime('%b')
        else:
            return ''
            
    def render_seasonEnd(self, value):
        if value:
            return '%s' % value.strftime('%b')
        else:
            return ''

def index(request):

    table = GroceryItemTable(GroceryItem.objects.all())
    table.paginate(page=request.GET.get("page", 1))
    table.order_by = request.GET.get("sort")

    ct={'table':table,
    }

    return render_to_response('recipemonkey/groceryitem/index.html',ct,context_instance=RequestContext(request))

def scan(request, id):
    
	try:
		i = GroceryItem.objects.get(pk=id)
	except GroceryItem.DoesNotExist:
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
			
			return redirect('recipemonkeyapp.views.groceryitem.scan',id=i.id)
			
	else:
		
		formset =StorageItemFormSet(queryset=i.storeditems())
		
	ct={'item':i,
		'formset':formset,
	}
		
	
	return render_to_response('recipemonkey/groceryitem/detail.html',ct,context_instance=RequestContext(request))	

def detail(request, id):
    
	try:
		i = GroceryItem.objects.get(pk=id)
	except GroceryItem.DoesNotExist:
		raise Http404


	
	ct={'item':i,
	}
	
	return render_to_response('recipemonkey/groceryitem/detail.html',ct,context_instance=RequestContext(request))

def barcodeimg(request, id):
    
	try:
		i = GroceryItem.objects.get(pk=id)
	except GroceryItem.DoesNotExist:
		raise Http404

	response=HttpResponse(content_type='image/png')

	url="https://%s/recipemonkeyapp/groceryitem/scan/%s/" % ('recipemonkey.getoutsideandlive.com',i.id)
	
	#img=barcode('qrcode',url,options=dict(eclevel='M'), margin=0, data_mode='8bits')   # Generates PIL.EpsImageFile instance
	img=barcode('qrcode',url,data_mode='8bits')
	#img=img.resize((90,90))

	img.save(response, 'PNG')
	
	return response