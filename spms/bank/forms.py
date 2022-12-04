from django.forms import ModelForm
from django import forms
from .models import CourseOutline , Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['semester', 'year','duration','mark','question','course_q','correctAns']
        widgets={
            'semester':forms.Select(attrs={'class':'form-control','placeholder':'Select'}),
            'year':forms.TextInput(attrs={'class':'form-control'}),
            'duration':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter duration, example: 15 mins'}),
            'mark':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter weight'}),
            'question':forms.Textarea(attrs={'class':'form-control','placeholder':'Type your question here'}),
            'course':forms.Select(attrs={'class':'form-control','placeholder':'Select'}),
            'correctAns':forms.Textarea(attrs={'class':'form-control','placeholder':'Type your answer here'})
        }

class CourseOutlineForm(ModelForm):
    class Meta:
        model=CourseOutline
        fields=['CourseTitle','year','semester', 'courseCode','courseResource','duration','PreRequisite','credit', 'contactHour','grading','assesment']

