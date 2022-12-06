from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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
from .filters import QuestionFilter,CourseOutlineFilter

from django.forms import formset_factory
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import View

# Create your views here.
def login_user(request):
    #form=LoginForm(request.POST or None)
    if request.method=="POST":
        #if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None: #and is_admin:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.success(request, ("There was an error logging in, Try again"))
                return redirect('login')
    else:
        return render(request, "bank/login.html", {})

def signout(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return render('Signout') 
        
    

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
    form=QuestionForm()
    AnswerFormSet=formset_factory(AnswerForm,extra=3)
    formset=AnswerFormSet()
    if request.method=='POST':
        # print(request.POST)
        form=QuestionForm(request.POST)

        formset=AnswerFormSet(request.POST)
        print(formset.is_valid(),form.is_valid(),form.cleaned_data)
        if form.is_valid() and formset.is_valid():
            question=form.save()
            # print(question,84)
            for f in formset:
                ansInst=Answer.objects.create(
                    ans=f.cleaned_data.get('ans'),
                    q_pk=question,
                )
                ansInst.save()
                print(ansInst)
        
    
    context={'form':form,'formset':formset}
    return render(request, 'bank/newQuestion.html', context)

#Show all questions
def drafts(request):
    questions=Question.objects.all()
    myFilter=QuestionFilter(request.GET, queryset=questions)
    questions=myFilter.qs
    context={'questions':questions,'myFilter':myFilter}

    return render(request, 'bank/viewQuestions.html',context)

#Show one question with details
def showQuestion(request,question_id):
    question=Question.objects.get(pk=question_id)
    answers=Answer.objects.filter(q_pk=question)
    context={'question':question,'answers':answers} 
    return render(request,'bank/showQuestion.html', context)

#Update questions
def updateQuestion(request,question_id):
    question=Question.objects.get(pk=question_id)
    # answers=Answer.objects.filter(q_pk=question)
    form=QuestionForm(request.POST or None,instance=question)
    # AnswerFormSet=formset_factory(AnswerForm)
    # formset=AnswerFormSet()
    # questions=form.save()
    # print(question,84)
    if form.is_valid():
        form.save()
        return redirect('drafts_')
    # for f in answers:
    #     ansInst=Answer.objects.update(
    #         ans=f.cleaned_data.get('ans'),
    #         q_pk=questions,
    #     )
    #     ansInst.save()

    context={'question':question,'form':form}
    return render(request, 'bank/updateQuestion.html',context)

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
    # total_duration=0
    for q in question:
        total_marks+=q.mark
        # total_duration+=q.duration
    num=0
    data.append("Total marks: "+str(total_marks))
    data.append(" ")
    data.append("Total duration: "+str(50))
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


###############Course OUtline#####################

def createCourseOutline(request):
    form=CourseOutlineForm()
    COFormSet=formset_factory(COForm, extra=7)
    PLOFormSet=formset_factory(PLOForm, extra=5)
    formset_=PLOFormSet
    formset=COFormSet
    if request.method=='POST':
        form=CourseOutlineForm(request.POST)
        formset=COFormSet(request.POST)
        formset_=PLOFormSet(request.POST)
        if form.is_valid() and formset.is_valid() and formset_.is_valid():
            outline=form.save()
            for f in formset:
                coInst=CO.objects.create(
                        CONo=f.cleaned_data.get('CONo'),
                        Domain=f.cleaned_data.get('Domain'),
                        Level=f.cleaned_data.get('Level'),
                        Statement=f.cleaned_data.get('Statement'),
                        out_pk=outline,
                    )
                coInst.save()
            for p in formset_:
                poInst=PLO.objects.create(
                        PLONo=p.cleaned_data.get('PLONo'),
                        PLOTitle=p.cleaned_data.get('PLOTitle'),
                        PLODescription=p.cleaned_data.get('PLODescription'),
                        outly_pk=outline,
                    )
                poInst.save()
    context={'form':form,'formset':formset,'formset_':formset_}
    return render(request, 'bank/courseoutlineForm.html',context)

def drafts_outline(request):
    courseOutline=CourseOutline.objects.all()
    myFilter=CourseOutlineFilter(request.GET, queryset=courseOutline)
    courseOutline=myFilter.qs
    context={'courseOutline':courseOutline,'myFilter':myFilter}

    return render(request, 'bank/courseOutline_drafts.html',context)

def viewOutline(request,outline_id):
    courseOutline=CourseOutline.objects.get(pk=outline_id)
    context={'courseOutline':courseOutline}
    return render(request, 'bank/viewOutline.html',context)

# #Delete course outlines
def deleteOutline(request, outline_id):  
    outlines = CourseOutline.objects.get(pk=outline_id)  
    outlines.delete()  
    return redirect('drafts_Outline') 

def showStatus(request):
    return render(request, 'bank/courseOutline_status.html')

def browseOutline(request):
    courseOutline=CourseOutline.objects.all()
    return render(request,'bank/browse_courseOutline.html', {'courseOutline':courseOutline} )

def editCourseOutline(request,courseOutline_id):
    outlines=CourseOutline.objects.get(pk=courseOutline_id)
    form=CourseOutlineForm(request.POST or None,instance=outlines)
    if form.is_valid():
        form.save()
        return redirect('drafts_Outline')
    return render(request, 'bank/editCourseOutline.html',{'outlines':outlines,'form':form})

# Generate single pdf of all questions
def outlines_pdf(request):
    buf = io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textobj=c.beginText()
    textobj.setTextOrigin(inch,inch)
    textobj.setFont("Helvetica",14)

    outlines=CourseOutline.objects.all()
    data=[]

    data.append("Combined Course Outlines")
    data.append(" ")
    data.append("_________________________________________")
    data.append(" ")
    data.append(" ")
    for q in outlines:
        data.append("Course Title: "+str(q.CourseTitle))
        data.append("Course Code: "+str(q.courseCode))
        data.append("Prerequisites: "+str(q.PreRequisite))
        data.append("Year: "+str(q.year))
        data.append("Semester: "+str(q.semester))
        data.append("Credits: "+str(q.credit))
        data.append("Contact Hours: "+str(q.contactHour))
        data.append("Duration: "+str(q.duration))
        data.append("Assessment: "+str(q.assesment))
        data.append("Grading: "+str(q.grading))
        data.append(" ")
        data.append("_________________________________________")
        data.append(" ")
        data.append(" ")

    for line in data:
        textobj.textLine(line)
    
    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True, filename='course_outlines.pdf')