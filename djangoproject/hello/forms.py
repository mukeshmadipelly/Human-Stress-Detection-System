from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser

class UserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'username')

class AuthenticationForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'password')

