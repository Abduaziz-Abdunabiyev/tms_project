from django import forms
from .models import PlannedLoad

class PlannedLoadForm(forms.ModelForm):
    pickup_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    delivery_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PlannedLoad
        fields = [
            'custom_load_number', 'customer', 
            'shipper', 'pickup_date', 'pickup_instructions',
            'consignee', 'delivery_date', 'delivery_instructions', 
            'bol'
        ]
