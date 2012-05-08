from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from recipemonkeyapp.models import Recipe
from django.http import HttpResponse,HttpResponseRedirect
from elaphe import barcode 
from django.http import Http404


#@login_required(login_url='/accounts/login/')
#def limited_object_detail(*args, **kwargs):
#    return object_detail(*args, **kwargs)


def index(request):
	
	recipe_list=Recipe.objects.all()
	
	
		
	ct={'recipe_list':recipe_list,
	
	}
	return render_to_response('recipemonkey/index.html',ct,context_instance=RequestContext(request))
	


def barcodes(request):

    import os
    import subprocess
    from tempfile import mkdtemp, mkstemp
    from django.template.loader import render_to_string
    import glob

    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=barcodes.pdf'

    barcodes_list=[]
    tmp_folder = mkdtemp()
    os.chdir(tmp_folder)        
    texfile, texfilename = mkstemp(dir=tmp_folder)
   
    for i in range(1,66):
        url="https://%s/recipemonkeyapp/scan/%s/" % ('mothership.getoutsideandlive.com',i)

        img=barcode('qrcode',url,data_mode='8bits',margin=0)
        from PIL import Image
        import numpy as np

        pix = np.asarray(img)

        pix = pix[:,:,0:3] # Drop the alpha channel
        idx = np.where(pix-255)[0:2] # Drop the color when finding edges
        box = map(min,idx)[::-1] + map(max,idx)[::-1]

        region = img.crop(box)
        f, fname = mkstemp(dir=tmp_folder,suffix=".eps")
        
        
        region.save(fname, 'EPS')
        barcodes_list.append({'code':i,'name':os.path.basename(fname)})
        f=None

    
   
    # In a temporary folder, make a temporary file
    
    # Pass the TeX template through Django templating engine and into the temp file
    os.write(texfile, render_to_string('recipemonkey/tex/barcodes.tex', {'barcodes': barcodes_list}))
    os.close(texfile)
    # Compile the TeX file with PDFLaTeX
    process=subprocess.Popen(['/usr/texbin/latex', texfilename],env={"PATH": "/usr/texbin"})

    if process.wait() != 0:
        raise Exception("There were some errors running latex")

    process=subprocess.Popen(['/usr/local/bin/dvipdf','-sPAPERSIZE=a4',texfilename+".dvi",texfilename+".pdf"],env={"PATH": "/usr/texbin:/usr/local/bin"})

    if process.wait() != 0:
        raise Exception("There were some errors generating pdf")

    # Move resulting PDF to a more permanent location
    
    
    
    dest=os.path.join('/usr/local/web/django/www/production/mothership',texfilename + '.pdf')
    #os.rename(texfilename + '.pdf', dest)
    # Remove intermediate files
   

    f2 = open(texfilename + '.pdf', 'r')
    response.write(f2.read())
    f2.close

    os.remove(texfilename)
    os.remove(texfilename + '.dvi')
    
    os.remove(texfilename + '.aux')
    os.remove(texfilename + '.log')
    os.remove(texfilename + '.pdf')
    
    for filename in glob.glob('*.eps') :
       os.remove( filename )

    os.rmdir(tmp_folder)
  


    return response

def scan(request, id):

    from recipemonkeyapp.models import StorageItem
    from django.forms import ModelForm

    class StorageItemForm(ModelForm):
        
        content = forms.ModelMultipleChoiceField(queryset=Recipe.objects.all())
        class Meta:
            model = StorageItem
            

    try:
        i = StorageItem.objects.get(barcode=id)
        form=StorageItemForm(instance=i)
    except StorageItem.DoesNotExist:
        form=StorageItemForm()

   

    ct={
        'form':form,
    }


    return render_to_response('recipemonkey/storage/item_detail.html',ct,context_instance=RequestContext(request))	

