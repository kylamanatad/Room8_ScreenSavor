from django.urls import path
from . import views

app_name = 'recommendation'

urlpatterns = [
    # path('', views.index, name='index'), #127.0.0.1/account
    path('', views.index, name='index'),  # 127.0.0.1/account
    path('recommendationregister/', views.RecommendationRegistration.as_view(), name='recommendationregister'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.Login.as_view(), name='login'),
]
