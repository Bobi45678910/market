from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''
            field.widget.attrs['class'] = 'form-control'
