from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Product


class ProductForm(forms.ModelForm):
    forms.TextInput(attrs={'required': True, 'autocomplete': 'off', 'class': 'form-control'})
    
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))