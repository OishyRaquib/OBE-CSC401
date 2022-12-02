from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from pyexpat.errors import messages
from django.http import HttpResponse
from django.http import JsonResponse

from .models import * 
from .forms import QuestionForm

def dashboard(request):
    return render(request, 'bank/facultydash.html')

def createQuestion(request):
    form=QuestionForm()
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request, 'bank/newQuestion.html', context)

def bank(request):
    return render(request, 'bank/viewQuestions.html')

def Login(request):
    if request.method=='POST':
        Username=request.POST['username']
        Password=request.POST['password']

        User=authenticate(userID=Username, password=Password)

        if User is not None:
            login(request, User)
            fname=User.name
            return render(request, 'bank/navbar.html', {'fname': fname})
        else:
            messages.error(request, "Wrong Credentials")
            return redirect('signout')

        
    return render(request, "bank/login.html")

def signout(request):
    pass