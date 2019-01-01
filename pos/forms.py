from django import forms
from pos.models import Word

POS = [
    ('Noun ', 'Noun'),
    ('Pronoun', 'Pronoun'),
    ('Verb', 'Verb'),
    ('Others', 'Others')
]


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'pos']
        widgets = {
            'word': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "Enter word", 'type': "text", 'name': 'q'}),
            'pos': forms.Select(
                attrs={'class': "btn btn-info dropdown-toggle", 'type': "button", "data-toggle": "dropdown",
                       "aria-haspopup": "true", "aria-expanded": "false"
                       }),

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
