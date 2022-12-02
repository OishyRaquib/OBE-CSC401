from django.forms import ModelForm
from .models import Question

class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=['semester', 'year','duration','mark','question','correctAns']
