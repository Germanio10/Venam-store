from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-grp"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-grp"
    }))
    company_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-grp"
    }))
    country = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-grp"
    }))
    street = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-grp"
    }))
    town = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-grp"
    }))
    state = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-grp"
    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-grp"
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-grp"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-grp"
    }))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'company_name',
                  'country', 'street', 'town', 'state', 'zip', 
                  'phone', 'email')
