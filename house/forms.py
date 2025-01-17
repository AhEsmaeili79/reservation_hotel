from django import forms
from .models import House, Review

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'image', 'image2', 'image3', 'image4', 'image5', 'city', 'number_of_rooms', 'area', 'number_of_parkings', 'capacity', 'price_per_day', 'pool', 'oven']
        
        # Custom widgets to apply styles
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'نام موضوع'}),
            'image': forms.ClearableFileInput(attrs={'class': 'input-field', 'accept': 'image/*'}),
            'image2': forms.ClearableFileInput(attrs={'class': 'input-field', 'accept': 'image/*'}),
            'image3': forms.ClearableFileInput(attrs={'class': 'input-field', 'accept': 'image/*'}),
            'image4': forms.ClearableFileInput(attrs={'class': 'input-field', 'accept': 'image/*'}),
            'image5': forms.ClearableFileInput(attrs={'class': 'input-field', 'accept': 'image/*'}),
            'city': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'شهر'}),
            'number_of_rooms': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'تعداد اتاق'}),
            'area': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'متراژ'}),
            'number_of_parkings': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'تعداد پارکینگ'}),
            'capacity': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'ظرفیت'}),
            'price_per_day': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'قیمت هر روز'}),
            'pool': forms.CheckboxInput(attrs={'class': 'input-checkbox'}),
            'oven': forms.CheckboxInput(attrs={'class': 'input-checkbox'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(HouseForm, self).__init__(*args, **kwargs)
        # Apply additional styles to each form field dynamically
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input-field'  # Add a common class for styling

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
