from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-grp'
    }))
    
    class Meta:
        model = Review
        fields = ("text",)
