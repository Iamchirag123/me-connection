#form.py
from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import company

class CompanyForm(ModelForm):
    class Meta:
        model = company
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }