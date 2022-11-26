from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.http import JsonResponse

from .models import *
from .forms import QuestionForm
# Create your views here.
# def login(request):
#     return render(request, 'bank/login.html')

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