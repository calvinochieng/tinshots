# forms.py
from django import forms
from .models import Booking, ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Your Phone'}),
            'message': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Your Message'}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['shoot_type', 'full_name', 'phone', 'email', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'input'}),
            'shoot_type': forms.Select(attrs={'class': 'input'}),
            'full_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Full Name'}),
            'phone': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
        }
