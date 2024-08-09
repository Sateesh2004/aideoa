# forms.py
from django import forms
from .models import JobShift

class JobShiftForm(forms.ModelForm):
    class Meta:
        model = JobShift
        fields = ['username', 'current_company', 'desired_company', 'mobile_no', 'email']
