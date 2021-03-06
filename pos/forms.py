from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    # declare the fields you will show
    username = forms.CharField(label="Your Username")
    # first password field
    password1 = forms.CharField(label="Your Password")
    # confirm password field
    password2 = forms.CharField(label="Repeat Your Password")
    email = forms.EmailField(label="Email Address")
    first_name = forms.CharField()
    last_name = forms.CharField(label="Surname")

    # this sets the order of the fields
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2",)
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "Enter your name", 'type': "text"}),
            'password1': forms.PasswordInput(
                attrs={'class': "form-control", 'placeholder': "Password", 'type': "password"}),

        }

    # this redefines the save function to include the fields you added
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()

        return user
