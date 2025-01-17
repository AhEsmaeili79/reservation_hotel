from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import  Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['arrive_date', 'exit_date', 'count_of_passengers']
        widgets = {
            'arrive_date': forms.DateInput(attrs={'type': 'text'}),
            'exit_date': forms.DateInput(attrs={'type': 'text'}),
        }

