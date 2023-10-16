from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-grp'
    }))

    class Meta:
        model = Review
        fields = ("text",)


class PriceFilterForm(forms.Form):
    min_price = forms.DecimalField(label='Min Price', required=False)
    max_price = forms.DecimalField(label='Max Price', required=False)
