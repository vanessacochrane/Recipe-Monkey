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
        barcodes_list.append(26)

    t = loader.get_template('recipemonkey/tex/barcodes.tex')

    import os
    from subprocess import call
    from tempfile import mkdtemp, mkstemp
    from django.template.loader import render_to_string
    # In a temporary folder, make a temporary file
    tmp_folder = mkdtemp()
    os.chdir(tmp_folder)        
    texfile, texfilename = mkstemp(dir=tmp_folder)
    # Pass the TeX template through Django templating engine and into the temp file
    os.write(texfile, render_to_string('recipemonkey/tex/barcodes.tex', {'barcodes': barcodes_list}))
    os.close(texfile)
    # Compile the TeX file with PDFLaTeX
    call(['pdflatex', texfilename], shell=True)
    # Move resulting PDF to a more permanent location
    
    
    
    dest=os.path.join('/usr/local/web/django/www/production/mothership',texfilename + '.pdf')
    os.rename(texfilename + '.pdf', dest)
    # Remove intermediate files
   

    f2 = open(dest, 'r')
    response.write(f2.read())
    f2.close

    os.remove(texfilename)
    os.remove(texfilename + '.aux')
    os.remove(texfilename + '.log')
    os.remove(texfilename + '.pdf')
    
    os.rmdir(tmp_folder)
  


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