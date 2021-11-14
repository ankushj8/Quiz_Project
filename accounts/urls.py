from django.urls import path
from . import views

urlpatterns = [
    path("Register", views.Register, name = "Register"),
    path("Sign_in", views.Sign_in, name = "Sign_in"),
    path("Sign_out", views.Sign_out, name = "Sign_out")
]