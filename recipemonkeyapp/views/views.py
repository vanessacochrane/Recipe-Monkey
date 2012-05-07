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

    from os import remove, rename
    from os.path import dirname
    from tempfile import NamedTemporaryFile
    import subprocess
    from django.template import Context, loader
    

    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=barcodes.pdf'

    barcodes_list=[]

    i=1
    for i in range(65):
        barcodes_list.append(i)


    t = loader.get_template('recipemonkey/barcodes.tex')

    c = Context({
        'barcodes': barcodes_list,
    })

    r = t.render(c)
    tex = NamedTemporaryFile()
    tex.write(r)
    tex.flush()
    base = tex.name


    path="/Volumes/ExtDisk2-2tb/Data/dropbox-cochranedavey/Dropbox/CochraneDavey/Development/Django/cochranedavey/"
    retcode = subprocess.check_call(["/usr/texbin/latex",base+'.tex'])
    retcode = subprocess.check_call(["/usr/local/bin/dvipdf",base+".dvi"])
    remove(names['log'])
    remove(names['aux'])

    f2 = open(base+'.pdf','r')
    response.write(f2.read())
    f2.close


    items = "log aux pdf dvi png".split()
    names = dict((x, '%s.%s' % (base, x)) for x in items)


    return response



def barcodes_old(request):

    barcodes_list=[]
    
    i=1
    for i in range(65):
        barcodes_list.append(i)


    ct={'barcodes':barcodes_list,
        'labels_per_page': 65+1,

    }

    return render_to_response('recipemonkey/labels.html',ct,context_instance=RequestContext(request))


def barcodeimg(request, code):


    response=HttpResponse(content_type='image/png')

    url="https://%s/recipemonkeyapp/scan/%s/" % ('mothership.getoutsideandlive.com',code)

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