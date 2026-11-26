from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'birth_date', 'avatar']

        labels = {
            'nickname': 'Никнейм',
            'birth_date': 'Дата рождения',
            'avatar': 'Изменить аватарку',
        }

        widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder': 'Введите никнейм',
                'autocomplete': 'off',
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
            }),
            'avatar': forms.FileInput(attrs={
                'accept': 'image/*',
            }),
        }