from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 
            'email', 'description', 'category',
        ) 

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Escreva aqui'
                }
            )
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
                'last_name',
                ValidationError(
                    'Primeiro nome não pode ser igual ao sobrenome',
                    code='invalid'
                )
            )

        return super().clean()
                