import floppyforms as forms
#from django.forms import ModelForm
from recipemonkeyapp.models import StorageItem, Recipe, GroceryItem
#from django.forms import extras
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

    
class DatePicker(forms.DateInput):
    template_name = 'datepicker.html'

    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
        )
        css = {
            'all': (
                'css/jquery-ui.css',
            )
        }


class StorageItemForm(forms.ModelForm):

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


    date_added = forms.DateField(widget=DatePicker)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-storageitem'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))
        
        super(StorageItemForm, self).__init__(*args, **kwargs)

    
    class Meta:
        model = StorageItem
        exclude = ('object_id','content_object','content_type')
        
       
class QuantitySlider(forms.RangeInput):
    min = 1
    max = 9999
    step = 1
    template_name = 'slider.html'

    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
        )
        css = {
            'all': (
                'css/jquery-ui.css',
            )
        }

# Create the form class.
class UpdateStorageItemForm(forms.ModelForm):


    quantity = forms.IntegerField(widget=QuantitySlider)

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if not 1 <= quantity <= 9999:
            raise forms.ValidationError("Enter a value between 1 and 9999")
        return quantity

    class Meta:
        model = StorageItem
        fields = ['quantity']

