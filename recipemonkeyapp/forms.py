from django import forms
from django.forms import ModelForm
from recipemonkeyapp.models import StorageItem
from django.forms import extras

# Create the form class.
class StorageItemForm(ModelForm):
	
	
	#date=forms.DateField(widget=widgets.AdminDateWidget())
	
	date=forms.DateField(widget=extras.SelectDateWidget)
	
	class Meta:
		model = StorageItem
		fields = ('id','storage','quantity','date')
	
	def __init__(self, *args, **kwargs):
		super(StorageItemForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		