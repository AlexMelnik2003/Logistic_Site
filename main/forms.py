from django import forms
from .models import Faq, Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['questions']
        widgets = {
            'questions': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Напишите сюда вопрос или предложение'}),
        }
