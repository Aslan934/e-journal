from django import forms

from . import models


class LoginForm(forms.Form):
    email = forms.CharField(label='Your email')
    password = forms.CharField(
        widget=forms.PasswordInput, label='Your password')


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.Teacher
        fields = ['email', 'name', 'password']

    def clean(self):
        email = self.cleaned_data.get("email")
        name = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

        values = {
            "email": email,
            'name': name,
            "password": password
        }
        return values
