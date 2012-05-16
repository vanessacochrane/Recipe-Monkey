from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from recipemonkeyapp.models import Recipe,GroceryItem
from django.http import HttpResponse,HttpResponseRedirect
from elaphe import barcode 
from django.http import Http404
import logging
from recipemonkeyapp.models import StorageItem
from django.forms import ModelForm
from django import forms
from django.db import models
from django.contrib.contenttypes.models import ContentType

#@login_required(login_url='/accounts/login/')
#def limited_object_detail(*args, **kwargs):
#    return object_detail(*args, **kwargs)

def savedsearch(request):
	
	
	ct={}
	
	return render_to_response('recipemonkey/savedsearches.html',ct,context_instance=RequestContext(request))



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


def ajax_object_request(request):
    # Expect an auto 'type' to be passed in via Ajax and POST
    #if request.is_ajax() and request.method == 'POST':
    
    #print request.GET
    #print request.GET.get('obj_type','')
    
    if request.GET.get('obj_type','') == 'R':
        objects = Recipe.objects.all() 
    else:
        objects = GroceryItem.objects.all() 

    return render_to_response('recipemonkey/storage/ajax_object_request.html', locals())


def send_expiry_notifications(request):
    from django.conf import settings
    from datetime import *
    if "notification" in settings.INSTALLED_APPS:
        from notification import models as notification
    else:
        notification = None
    
    from django.contrib.auth.models import User
    
    u = User.objects.all()

    items = StorageItem.objects.all()
    
    expiring=[]
    for i in items:
        if i.expiry - date.today() < timedelta(days=5):
            expiring.append(i)
    
    if notification:
        notification.send(u, "storage_nearing_expiry",{'items':items,'expiring':expiring} )


    return redirect('recipemonkeyapp.views.views.index')

class StorageItemForm(ModelForm):
    
    CHOICES=(('-','--Choose--'),('R','Recipe'),('I','Ingredient'))
    obj_type=forms.ChoiceField(label='Object Type',widget=forms.Select(attrs={'onchange':'get_objects();'}), choices=CHOICES)
    
    recipes = [(r.id, r.name) for r in Recipe.objects.all()]
    items = [(r.id, r.name) for r in GroceryItem.objects.all()]
    
    OBJ_CHOICES = recipes
    OBJ_CHOICES.extend(items)
    OBJ_CHOICES.insert(0,('-','--Select Type--'))
    
    
    obj = forms.ChoiceField(choices=OBJ_CHOICES,label='Object')
    
    #recipe = forms.ModelChoiceField(queryset=Recipe.objects.all(),required=False,widget=forms.Select(attrs={'onchange':'get_objects();'}))
    #ingredient = forms.ModelChoiceField(queryset=GroceryItem.objects.all(),required=False)
    barcode = forms.CharField(max_length=255,widget=forms.HiddenInput())


    date_added = forms.DateField(
                widget=forms.TextInput(attrs={'class':'datepicker'}))

    class Meta:
        model = StorageItem
        exclude = ('object_id','content_object','content_type')
        
        

class StorageUpdateForm(ModelForm):
    class Meta:
        model = StorageItem
        fields = ['quantity']


def scan(request, id, mode='NEW'):


    
    
    logging.debug('Scanned barcode %s' % id)
    


            
    try:
        si = StorageItem.objects.get(barcode=id)
        form=StorageUpdateForm(instance=si)
        
    except StorageItem.DoesNotExist:
        form=StorageItemForm({'barcode':id})
        si = None

    if request.method == 'POST': # If the form has been submitted...

        if si:
            form=StorageUpdateForm(request.POST,instance=si)
        else:
            form=StorageItemForm(request.POST,instance=si)
        
        if form.is_valid():
           
            nsi=form.save(commit=False)
            
            if not si:
        
                if form.cleaned_data['obj_type']=='R':
                    i=Recipe.objects.get(pk=form.cleaned_data['obj'])
                    nsi.content_object=i
                    nsi.object_id=i.id
                elif form.cleaned_data['obj_type']=='I':
                    i=GroceryItem.objects.get(pk=form.cleaned_data['obj'])
                    nsi.content_object=i
                    nsi.object_id=i.id
            

                nsi.content_type=ContentType.objects.get_for_model(nsi.content_object)

            
            logging.debug('trying to save storage item... %s' % nsi)
            nsi.save()
                

            return redirect('recipemonkeyapp.views.views.scan',id=nsi.barcode)

        else:
            logging.debug('form not valid...')
    ct={
        'item': si,
        'form':form,
    }


    return render_to_response('recipemonkey/storage/item_detail.html',ct,context_instance=RequestContext(request))	

