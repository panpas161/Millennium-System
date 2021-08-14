from django import forms
from .models import User

class loginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'