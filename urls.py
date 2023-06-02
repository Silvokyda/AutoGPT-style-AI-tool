from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_vulnerable_code, name="generate_vulnerable_code"),
]