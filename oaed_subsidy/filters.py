import django_filters
from django_filters import CharFilter,DateFilter,ModelChoiceFilter
from .models import *

class SubsidizedIndividualFilter(django_filters.FilterSet):
    q = CharFilter(method='searchMethod',label="Αναζήτηση")
    class Meta:
        model = SubsidizedIndividual
        fields = []

    def searchMethod(self,queryset, value):
        filter = queryset.filter
        queryset = filter(firstname__contains=value) or filter(lastname__contain=value) or filter()
        return queryset

class DepartmentFilter(django_filters.FilterSet):
    q = CharFilter(method='searchMethod',label="Αναζήτηση")
    class Meta:
        model = Department
        fields = []

    def searchMethod(self,queryset, value):
        filter = queryset.filter
        queryset = filter(name__contains=value)
        return queryset
