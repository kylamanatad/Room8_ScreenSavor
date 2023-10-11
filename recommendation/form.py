from django.forms import ModelForm
from django import forms
from .models import Recommendation
from .models import User


class RecommendationForm(ModelForm):
    user = forms.CharField(widget=forms.TextInput)
    movie = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Recommendation
        fields = ['user', 'movie']


class UserRegistration(ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.TextInput)
    firstName = forms.CharField(widget=forms.TextInput)
    lastName = forms.CharField(widget=forms.TextInput)
    emailAddress = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'firstName', 'lastName', 'emailAddress']


class LoginForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = ['username', 'password']
