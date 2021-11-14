from django.urls import path
from . import views

urlpatterns = [
    path('Quiz', views.Quiz, name = "Quiz" ),
    path('Score', views.Score, name = "Score" )
]