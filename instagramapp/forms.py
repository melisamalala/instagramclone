from .models import Image, Review, Profile
from django import forms
from django.forms import ModelForm, Textarea


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'likes']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class UpdatebioForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'followers', 'following']
