from django.db import models

# Create your models here.
class quizQuestion(models.Model):
    questionNo= models.IntegerField(default=0)
    question = models.TextField(default="question")
    optionA = models.CharField(max_length=50, default="null")
    optionB = models.CharField(max_length=50, default="null")
    optionC = models.CharField(max_length=50, default="null")
    optionD = models.CharField(max_length=50, default="null")
    correctAns = models.CharField(max_length = 50, default="null")
