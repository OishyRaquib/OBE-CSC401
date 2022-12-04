import django_filters
from django_filters import DateFilter

from .models import *

class QuestionFilter(django_filters.FilterSet):
    class Meta:
        model=Question
        fields="__all__"
        exclude=['duration','question','mark','correctAns']
