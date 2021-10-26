from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    model = Order
    fields = (
        'full_name',
        'email',
        'phone_number',
        'street_address1',
        'street_address2',
        'postcode',
        'town_or_city',
    )

    def __init__(self, *args, **kwargs):    
        """ Adds placeholders and classes to the form, removes auto labels and set focus on first field """
        
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Address Line 1',
            'street_address2': 'Address Line 2',
            'postcode': 'Postal Code',
            'town_or_city': 'Town Or City',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field.required]:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False