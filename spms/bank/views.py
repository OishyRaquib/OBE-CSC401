from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from .models import *
from .forms import QuestionForm
# Create your views here.
def login(request):
    return render(request, 'bank/login.html')

#Faculty dashboard
def dashboard(request):
    return render(request, 'bank/facultydash.html')



#Create a question
def createQuestion(request):
    form=QuestionForm
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # return HttpResponseRedirect('/createQuestion?submitted=True')
            except:
                pass
        

    context={'form':form}
    return render(request, 'bank/newQuestion.html', context)

#Show all questions
def drafts(request):
    questions=Question.objects.all()
    return render(request, 'bank/viewQuestions.html',{'questions':questions})

#Show one question with details
def showQuestion(request,question_id):
    question=Question.objects.get(pk=question_id)
    return render(request,'bank/showQuestion.html', {'question':question} )

#Update questions
def updateQuestion(request,question_id):
    question=Question.objects.get(pk=question_id)
    form=QuestionForm(request.POST or None,instance=question)
    if form.is_valid():
        form.save()
        return redirect('drafts_')
    return render(request, 'bank/updateQuestion.html',{'question':question, 'form':form})

# #Delete questions
def deleteQuestion(request, question_id):  
    question = Question.objects.get(pk=question_id)  
    question.delete()  
    return redirect('drafts_') 


#Student dashboard
def studash(request,pk_stu):
    student=Student.objects.get(id=pk_stu)
    
    prg=student.programID_set.all()
    dep=student.deptID_set.all()

    context={'student':student}
    return render(request, 'bank/studdash.html',context)