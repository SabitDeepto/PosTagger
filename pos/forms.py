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

        # def clean_word(self, *args, **kwargs):
        #     word = self.cleaned_data.get("word")
        #     x = str(word.split())
        #     return x


CHOICE = [
    ('Male', 'Male'),
    ('Female', 'Female')
]


class TestForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.CharField(widget=forms.Select(choices=CHOICE))
