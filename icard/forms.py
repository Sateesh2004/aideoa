# forms.py
from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'mobile_no','current_company',  'photo']
    first_name = forms.CharField(required=False)  
    last_name = forms.CharField(required=False)   
    email = forms.EmailField(required=False)      
    mobile_no = forms.CharField(required=False)   
    current_company = forms.CharField(required=False)   
    photo = forms.ImageField(required=False) 
