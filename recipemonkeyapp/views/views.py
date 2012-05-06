from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from recipemonkeyapp.models import Recipe
from django.http import HttpResponse,HttpResponseRedirect
from elaphe import barcode 

#@login_required(login_url='/accounts/login/')
#def limited_object_detail(*args, **kwargs):
#    return object_detail(*args, **kwargs)


def index(request):
	
	recipe_list=Recipe.objects.all()
	
	
		
	ct={'recipe_list':recipe_list,
	
	}
	return render_to_response('recipemonkey/index.html',ct,context_instance=RequestContext(request))
	

def barcodes(request):

    barcodes_list=[]
    
    i=1
    for i in range(30):
        barcodes_list.append(i)


    ct={'barcodes':barcodes_list,
        'labels_per_page': 30,

    }

    return render_to_response('recipemonkey/labels.html',ct,context_instance=RequestContext(request))


def barcodeimg(request, code):


	response=HttpResponse(content_type='image/png')

	url="https://%s/recipemonkeyapp/groceryitem/scan/%s/" % ('recipemonkey.getoutsideandlive.com',code)

	img=barcode('qrcode',url,data_mode='8bits',margin=0)
    from PIL import Image
    import numpy as np

    pix = np.asarray(img)

    pix = pix[:,:,0:3] # Drop the alpha channel
    idx = np.where(pix-255)[0:2] # Drop the color when finding edges
    box = map(min,idx)[::-1] + map(max,idx)[::-1]

    region = img.crop(box)
	region.save(response, 'PNG')

	return response