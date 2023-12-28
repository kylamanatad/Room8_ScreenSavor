from django.urls import path
from .views import LandingPage, RecommendationRegistration, RegisterUser, Login
from .views import OccasionView, GenreView, YearView, RatingView, RecommendationResults

app_name = 'recommendation'

urlpatterns = [
    path('', LandingPage.as_view(), name='landing_page'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('recommend/', RecommendationRegistration.as_view(), name='recommend_movie'),
    path('occasion/', OccasionView.as_view(), name='occasion'),
    path('genre/', GenreView.as_view(), name='genre'),
    path('year/', YearView.as_view(), name='year'),
    path('rating/', RatingView.as_view(), name='rating'),
    path('recos/', RecommendationResults.as_view(), name='recos'),
]

