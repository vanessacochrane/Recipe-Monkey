from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from recipemonkeyapp.models import Recipe

#@login_required(login_url='/accounts/login/')
#def limited_object_detail(*args, **kwargs):
#    return object_detail(*args, **kwargs)


def index(request):
	
	recipe_list=Recipe.objects.all()
	
	
		
	ct={'recipe_list':recipe_list,
	
	}
	return render_to_response('recipemonkey/index.html',ct,context_instance=RequestContext(request))
	
	
