from django.forms import ModelForm
from django import forms
from .models import CourseOutline , Question, Answer,CO,PLO

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['semester', 'year','duration','mark','question','course_ID']
        widgets={
            'semester':forms.Select(attrs={'class':'form-control','placeholder':'Select'}),
            'year':forms.TextInput(attrs={'class':'form-control'}),
            'duration':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter duration, example: 15 mins'}),
            'mark':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter weight'}),
            'question':forms.Textarea(attrs={'class':'form-control','placeholder':'Type your question here'}),
            'course_ID':forms.Select(attrs={'class':'form-control','placeholder':'Course ID'}),
            # 'correctAns':forms.Textarea(attrs={'class':'form-control','placeholder':'Type your answer here'})
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['ans']
        widgets={
            'ans':forms.Textarea(attrs={'class':'form-control','placeholder':'Type your answer here'})
        }



class CourseOutlineForm(ModelForm):
    class Meta:
        model=CourseOutline
        fields="__all__"
        # exclude=['plo_id']
        widgets={
            'CourseTitle':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'courseCode':forms.TextInput(attrs={'class':'form-control','placeholder':'Type your course ID'}),
            'courseResource':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'mob':forms.TextInput(attrs={'class':'form-control'}),
            'office':forms.TextInput(attrs={'class':'form-control'}),
            'course_descrip':forms.TextInput(attrs={'class':'form-control'}),
            'out_deptid':forms.TextInput(attrs={'class':'form-control'}),
            'credit':forms.NumberInput(attrs={'class':'form-control'}),
            'PreRequisite':forms.TextInput(attrs={'class':'form-control'}),
            'contactHour':forms.TextInput(attrs={'class':'form-control'}),

            'grading':forms.TextInput(attrs={'class':'form-control'}),
            'semester':forms.TextInput(attrs={'class':'form-control'}),
            'days':forms.TextInput(attrs={'class':'form-control','placeholder':'Example: 1:00-2:30pm MW'}),

            'year':forms.NumberInput(attrs={'class':'form-control'}),
            'duration':forms.TextInput(attrs={'class':'form-control','placeholder':'Total duration of class'}),
            'mark':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter total marks'}),
            'assessment':forms.TextInput(attrs={'class':'form-control'}),
            # 'correctAns':forms.Textarea(attrs={'class':'form-control','placeholder':'Type your answer here'})
        }


class COForm(forms.ModelForm):
    class Meta:
        model=CO
        fields=['CONo','Domain','Level','Statement']
        widgets={
            'CONo':forms.TextInput(attrs={'class':'form-control','placeholder':'Example: CO1'}),
            'Domain':forms.TextInput(attrs={'class':'form-control','placeholder':'Example: Cognitive'}),
            'Level':forms.NumberInput(attrs={'class':'form-control','placeholder':'Example: 1'}),
            'Statement':forms.TextInput(attrs={'class':'form-control'}),
            }

class PLOForm(forms.ModelForm):
    class Meta:
        model=PLO
        fields=['PLONo','PLOTitle','PLODescription']
        widgets={
            'PLONo':forms.TextInput(attrs={'class':'form-control','placeholder':'Example: PO1'}),
            'PLOTitle':forms.TextInput(attrs={'class':'form-control','placeholder':'Example: Engineering Knowledge'}),
            'PLODescription':forms.TextInput(attrs={'class':'form-control'}),
            }
        