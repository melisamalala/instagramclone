from .models import Image, Review
from django import forms
from django.forms import ModelForm, Textarea


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'likes']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [ 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }