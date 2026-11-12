
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'birth_date', 'avatar']

        widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder': 'Введите никнейм'
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }
