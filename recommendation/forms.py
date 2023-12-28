# recommendation/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Recommendation
from .models import Genre, MovieYear, MovieRating
from .models import User



class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['movie']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User  # Change this to your custom user model
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class OccasionForm(forms.Form):
    OCCASION_CHOICES = [
        ('alone', 'Just watching a movie by myself.'),
        ('date', 'Movie Date.'),
        ('friends', 'Movie Night with friends.'),
        ('date_night', 'Date Night with boyfriend or girlfriend.'),
        ('family', 'Watching a movie with family or relatives.'),
    ]

    occasion = forms.ChoiceField(choices=OCCASION_CHOICES, widget=forms.RadioSelect)

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        widgets = {
            'name': forms.CheckboxSelectMultiple,
        }

class YearForm(forms.ModelForm):
    class Meta:
        model = MovieYear
        fields = ['year']

class RatingForm(forms.ModelForm):
    class Meta:
        model = MovieRating
        fields = ['rating']
