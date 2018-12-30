
from django import forms
from pos.models import Word


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word']
        widgets = {
            'word': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "Enter word", 'type': "text", 'name': 'q'}),

        }
