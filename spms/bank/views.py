from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from pyexpat.errors import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.http import FileResponse
import io
# from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from .utils import render_to_pdf
# from django.views.generic import View

from .models import * 
from .forms import *
# Create your views here.
def login(request):
    return render(request, 'bank/login.html')

#Faculty dashboard
def dashboard(request):
    return render(request, 'bank/facultydash.html')

#Student dashboard
def studash(request,pk_stu):
    student=Student.objects.get(id=pk_stu)
    
    prg=student.programID_set.all()
    dep=student.deptID_set.all()

    context={'student':student}
    return render(request, 'bank/studdash.html',context)


#####QUESTION BANK###########

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

# Generate single pdf of all questions
def question_pdf(request):
    buf = io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textobj=c.beginText()
    textobj.setTextOrigin(inch,inch)
    textobj.setFont("Helvetica",14)

    question=Question.objects.all()
    data=[]
    print(len(question))

    data.append("Final Examinations 2022")
    data.append(" ")

    total_marks=0
    total_duration=0
    for q in question:
        total_marks+=q.mark
        total_duration+=q.duration
    num=0
    data.append("Total marks: "+str(total_marks))
    data.append(" ")
    data.append("Total duration: "+str(total_duration))
    data.append("_________________________________________")
    data.append(" ")
    data.append("Answer the following questions.")
    data.append(" ")
    data.append(" ")
    for q in question:
        # textobj.textLine(q)
        # data.append(q.semester)
        # data.append(q.year)
        # data.append(q.duration)
        # data.append(q.mark)
        data.append(str(num+1)+"."+q.question+"    "+str(q.mark)+" marks")
        data.append(" ")
        num+=1

    for line in data:
        textobj.textLine(line)
    
    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True, filename='question.pdf')

# Generate single question pdf
# def ques_pdf(request,question_id):
#     buf = io.BytesIO()
#     c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
#     textobj=c.beginText()
#     textobj.setTextOrigin(inch,inch)
#     textobj.setFont("Helvetica",14)

#     q=Question.objects.get(pk=question_id)
#     data=[]

#     data.append("Final Examinations "+q.year+" "+q.semester)
#     data.append(" ")

#     data.append("Total marks: "+str(q.mark))
#     data.append(" ")
#     data.append("Total duration: "+str(q.duration))
#     data.append("_________________________________________")
#     data.append(" ")
#     data.append("Answer the following questions.")
#     data.append(" ")
#     data.append(" ")
#     num=0
#     # for q in question:
#         # textobj.textLine(q)
#         # data.append(q.semester)
#         # data.append(q.year)
#         # data.append(q.duration)
#         # data.append(q.mark)
#     data.append(str(num+1)+"."+q.question+"    "+str(q.mark)+" marks")
#     data.append(" ")

#     for line in data:
#         textobj.textLine(line)
    
#     c.drawText(textobj)
#     c.showPage()
#     c.save()
#     buf.seek(0)

#     return FileResponse(buf,as_attachment=True, filename='question_.pdf')
