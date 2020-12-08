from django import forms
from .models import Client
from .models import Product
from .models import Contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('client', 'product', 'quantity',)
