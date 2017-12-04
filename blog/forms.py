from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'sername', 'phone', 'email', 'product_format',
                    'product_size', 'product', 'price']
