from . models import Review 
from django import forms 


class ReviewForm(forms.ModelForm):

    class Meta:
        model = review
        fields = ["title","content"]