from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from .views import protected_view, CustomLoginView

urlpatterns = [
    path("", views.hero, name='home'),
    path("hero", views.hero, name='hero'),
    path("signup", views.signup_views, name='signup'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('protected', protected_view, name='protected'),
]
  
   