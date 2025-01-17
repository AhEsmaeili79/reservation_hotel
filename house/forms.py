from django import forms
from .models import House, Review

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'image', 'image2', 'image3', 'image4', 'image5', 'city', 'number_of_rooms', 'area', 'number_of_parkings', 'capacity', 'price_per_day', 'pool', 'oven']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
