from django import forms
from .models import Client, Product, Order

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'middle_name', 'phone_number',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'stored',)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('client', 'product', 'quantity', 'date',)

