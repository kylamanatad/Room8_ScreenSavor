from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .form import RecommendationForm, UserRegistration, LoginForm


def index(request):
    return HttpResponse("Hello! Welcome!")


class RecommendationRegistration(View):
    template = 'recommendation.html'

    def get(self, request):
        address = RecommendationForm()
        return render(request, self.template, {'form': address})


class RegisterUser(View):
    template = 'user.html'

    def get(self, request):
        user = UserRegistration()
        return render(request, self.template, {'form': user})

    def post(self, request):
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/recommendation/login')

        return render(request, self.template, {'form': form})


class Login(View):
    template = 'login.html'

    def get(self, request):
        log = LoginForm()
        return render(request, self.template, {'form': log})
