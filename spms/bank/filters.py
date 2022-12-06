import django_filters
from django_filters import DateFilter

from .models import *

class QuestionFilter(django_filters.FilterSet):
    class Meta:
        model=Question
        fields=['course_ID','semester','year']
        # exclude=['duration','question','mark','correctAns']

class CourseOutlineFilter(django_filters.FilterSet):
    class Meta:
        model=CourseOutline
        fields=['courseCode','semester','year']

