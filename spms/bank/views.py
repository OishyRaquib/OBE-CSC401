from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from .models import * 
from .forms import QuestionForm, CourseOutlineForm
# Create your views here.
def Login(request):
    if request.method=='post':
        Username=request.POST['username']
        Pass1=request.POST['Password']
        User=authenticate(userID=Username, password=Pass1)

        if User is not None:
            login(request, User)
            fname=User.name
            return render(request, 'bank/navbar.html', {'fname': fname})
        else:
            messages.error(request, "Wrong Credentials")
            return redirect('Signout')
            
    return render(request, "bank/login.html")

def signout(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return render('Signout') 
        
    

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

    
#Course OUtline

def createCourseOutline(request):
    form=CourseOutlineForm
    if request.method=='POST':
        form=CourseOutlineForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
    context={'form':form}
    return render(request, 'bank/courseoutlineForm.html',context)

def drafts_outline(request):
    courseOutline=CourseOutline.objects.all()
    return render(request, 'bank/courseOutline_drafts.html',{'courseOutline':courseOutline})


def showStatus(request):


    return render(request, 'bank/courseOutline_status.html')

def browseOutline(request,pk_outline):
    courseOutline=CourseOutline.objects.get(id=pk_outline)
    return render(request,'bank/browse_courseOutline.html', {'courseOutline':courseOutline} )
