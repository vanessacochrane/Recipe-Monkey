from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from recipemonkeyapp.models import Storage



def index(request):
    	
	item_list=Storage.objects.all().order_by('expiry','desc')
	
	
		
	ct={'item_list':item_list,
	
	}
	
	return render_to_response('recipemonkey/storage/index.html',ct,context_instance=RequestContext(request))
