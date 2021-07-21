import django_filters
from django_filters import CharFilter,DateFilter,ModelChoiceFilter
from .models import *

class TeacherFilter(django_filters.FilterSet):
    q = CharFilter(method='searchMethod',label="Αναζήτηση")

    class Meta:
        model = Teacher
        fields = []

    def searchMethod(self, queryset, name, value):
        filter = queryset.filter
        queryset = filter(firstname__contains=value) or filter(lastname__contains=value) or filter(email__contains=value)
        return queryset

class SubjectReportFilter(django_filters.FilterSet):
    q = CharFilter(method='searchMethod',label="Αναζήτηση")

    class Meta:
        model = SubjectReport
        fields = []

    def searchMethod(self, queryset, name, value):
        filter = queryset.filter
        queryset = filter(teacher__contains=value)
        return queryset

class AttendanceReportFilter(django_filters.FilterSet):
    q = CharFilter(method='searchMethod',label="Αναζήτηση")

    class Meta:
        model = AttendanceReport
        fields = []

    def searchMethod(self, queryset, name, value):
        filter = queryset.filter
        queryset = filter(teacher__contains=value)
        return queryset