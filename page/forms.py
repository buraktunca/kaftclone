from django import forms
from django.forms import ModelForm
from .models import Carousel

class CarouselModelForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ['title','cover_image']
