from django.forms import ModelForm
from .models import CourseOutline, Question

class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=['semester', 'year','duration','mark','question','correctAns']

class CourseOutlineForm(ModelForm):
    class Meta:
        model=CourseOutline
        fields=['CourseTitle', 'courseCode','courseResource','duration','PreRequisite','credit', 'contactHour','grading','assesment']

