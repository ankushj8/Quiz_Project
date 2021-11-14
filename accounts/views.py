from typing import Dict
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

from QuizApp.models import quizQuestion

# Create your views here.

def Register(request):
    if request.method == "POST":
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        password = request.POST["password"]
        email = request.POST["email"]
        userName = request.POST["userName"]
        confirmPassword = request.POST["confirmPassword"]
        if User.objects.filter(username = userName).exists():
            messages.info(request, "Username taken!")
            return redirect("Register")
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email taken!")
            return redirect("Register")
        if password != confirmPassword:
            messages.info(request, "Passwords don't match!")
            return redirect("Register")
        else:
            user = User.objects.create_user(username = userName, password = password, last_name = lastName,
                                            first_name = firstName, email = email)
            user.save()
            return redirect("Sign_in")
    return render(request, "Register.html")
def Sign_in(request):
    if request.method == "POST":
        userName = request.POST["userName"]
        password =request.POST["password"]
        user = auth.authenticate(username = userName, password=password)
        if user is not None:
            auth.login(request, user)
            request.session["counter"] = 1
            request.session["length"] = len(quizQuestion.objects.all())
            request.session["ansDict"] = {}
            return redirect("Quiz")
        else:
            messages.error(request, "Invalid credentials!")
            return redirect("Sign_in")
    return render(request, "Sign_in.html")
def Sign_out(request):
    auth.logout(request)
    return redirect("Sign_in")