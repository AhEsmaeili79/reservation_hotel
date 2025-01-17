from django import forms
from .models import House,Review

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'image', 'city', 'number_of_rooms', 'area', 'number_of_parkings', 'capacity', 'price_per_day', 'pool', 'oven']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']