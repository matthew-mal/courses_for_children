from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=20, required=True, label='Login')
    email = forms.EmailField(max_length=50, required=True, label='Email')

    class Meta:
        model = Profile
        fields = ('username', 'email', 'first_name', 'last_name')


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, required=True, label='Login')
    email = forms.EmailField(max_length=50, required=True, label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True,
                             help_text='Обязательное поле. Введите действительный адрес электронной почты.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


