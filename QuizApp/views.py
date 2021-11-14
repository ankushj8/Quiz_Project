from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import quizQuestion
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def Quiz(request):
    if not request.user.is_authenticated:
        return redirect("Register")

    quesFields = quizQuestion.objects.get(id = 1)
    prePopulate = ""

    if request.method == "POST":
        counter = request.session["counter"]
        length = request.session["length"]
        quesFields = quizQuestion.objects.get(id = counter)
        print("Counter:", counter)
        # This line is purely for dummy data
        # For some reason the program doesn't run without it
        # Possible reason - request.session saves till second last update to variables
        request.session["dummy"] = "dummy"
        
        if request.POST["submit"] == "next":
            print("Inside next Func")
            if "options" not in request.POST:
                messages.warning(request, "Please select an option!")
                return render(request, "Quiz.html", {"quesFields": quesFields})
            userAns = request.POST["options"]
            request.session["ansDict"][str(counter)] = userAns
            print("AnsDict:", request.session["ansDict"])
            print("User Answer:", userAns)
            if counter >0 and counter <length:
                if str(counter+1) in request.session["ansDict"]:
                    prePopulate = request.session["ansDict"][str(counter + 1)]
                quesFields = quizQuestion.objects.get(id = counter+1)
                request.session["counter"] += 1
            if counter == length:
                # Final Submit logic here
                print("Towards score page")
                return redirect("Score")
        if request.POST["submit"] == "prev":
            print("Inside prev Func")
            if counter > 1 and counter <=length:
                prePopulate = request.session["ansDict"][str(counter - 1)]
                quesFields = quizQuestion.objects.get(id = counter-1)
                request.session["counter"] -= 1
    return render(request, "Quiz.html", {"quesFields": quesFields, "prePopulate":prePopulate})

def Score(request):
    length = request.session["length"]
    ansDict = request.session["ansDict"]
    noOfCorrect = 0
    print("ansDict", ansDict)
    for i in range(length):
        if ansDict[str(i+1)] == quizQuestion.objects.get(id = i+1).correctAns:
            noOfCorrect += 1
    percent = 100*noOfCorrect/length
    return render(request, "Score.html", {"noOfCorrect":noOfCorrect, "percent":percent})