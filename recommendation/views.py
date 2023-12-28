# recommendation/views.py
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import RecommendationForm, LoginForm, OccasionForm, GenreForm, YearForm, RatingForm
from django.contrib.auth import login
from .models import User
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RegisterForm

class LandingPage(View):
    template = 'landing_page.html'

    def get(self, request):
        return render(request, self.template)

class RecommendationRegistration(View):
    template = 'feelings.html'

    def get(self, request):
        form = RecommendationForm()
        return render(request, self.template, {'form': form})

class RegisterUser(View):
    template = 'register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password1'],
            )

            # Log in the user after successful registration
            login(request, new_user)

            messages.success(request, 'Registration successful! You are now logged in.')

            # Redirect to a different page after successful registration
            return redirect(reverse('recommendation:login'))
        else:
            # Form is not valid, re-render the registration page with errors
            messages.error(request, 'Please fill in all required fields and provide valid information.')
            return render(request, self.template, {'form': form})

class Login(View):
    template = 'login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('recommendation:recommend_movie')

            else:
                messages.error(request, 'Invalid login credentials')
        return render(request, self.template_name, {'form': form})

class OccasionView(View):
    template_name = 'occasion.html'

    def get(self, request):
        form = OccasionForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = OccasionForm(request.POST)
        if form.is_valid():
            selected_occasion = form.cleaned_data['occasion']
            # You can perform actions based on the selected occasion here
            return redirect('recommendation:genre')
        return render(request, self.template_name, {'form': form})

class GenreView(View):
    template_name = 'genre.html'

    def get(self, request):
        form = GenreForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = GenreForm(request.POST)
        if form.is_valid():
            selected_genres = form.cleaned_data['name']
            # Process selected genres as needed
            return redirect('recommendation:genre')  # Redirect to the genre page
        return render(request, self.template_name, {'form': form})

class YearView(View):
    template_name = 'year.html'

    def get(self, request):
        form = YearForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = YearForm(request.POST)
        if form.is_valid():
            # Process the form data (save to session or database)
            selected_year = form.cleaned_data['year']
            # You can store the selected_year in the session or process as needed

            # Redirect to the next page (adjust 'next_page_url' accordingly)
            next_page_url = 'next_page_url'  # Replace with the actual URL of the next page
            return redirect(next_page_url)
        else:
            # Form is not valid, render the page again with errors
            return render(request, self.template_name, {'form': form})

class RatingView(View):
    template_name = 'rating.html'

    def get(self, request):
        form = RatingForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            # Process the form data (save to session or database)
            selected_rating = form.cleaned_data['rating']
            # You can store the selected_rating in the session or process as needed

            # Redirect to the next page (adjust 'next_page_url' accordingly)
            # next_page_url = 'next_page_url'  # Replace with the actual URL of the next page
            # return redirect(next_page_url)
        else:
            # Form is not valid, render the page again with errors
            return render(request, self.template_name, {'form': form})

class RecommendationResults(View):
    template_name = 'recos.html'

    def get(self, request):
        # Add any logic to fetch or process recommendations data
        recommendations = []  # Replace with your actual data
        context = {'recommendations': recommendations}
        return render(request, self.template_name, context)
