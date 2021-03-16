import django_filters
from django_filters import CharFilter,DateFilter
from .models import *

class SubsidizedBusinessFilter(django_filters.FilterSet):
    q = CharFilter(method='searchmethod',label="Αναζήτηση")
    start_date = DateFilter(field_name="entrydate",lookup_expr="gte",label="Από")
    end_date = DateFilter(field_name="entrydate",lookup_expr="lte",label="Έως")

    class Meta:
        model = SubsidizedBusiness
        fields = []

    def searchmethod(self, queryset, name, value):
        filter = queryset.filter
        queryset = filter(firstname__contains=value) or filter(lastname__contains=value) or filter(companytype__contains=value) \
        or filter(companyname__contains=value) or filter(phonenumber__contains=value) or filter(cellphone__contains=value)
        return queryset

class InterestedBusinessFilter(django_filters.FilterSet):
    q = CharFilter(method='searchmethod',label="Αναζήτηση")
    start_date = DateFilter(field_name="entrydate",lookup_expr="gte",label="Από")
    end_date = DateFilter(field_name="entrydate",lookup_expr="lte",label="Έως")

    class Meta:
        model = InterestedBusiness
        fields = []

    def searchmethod(self,queryset, name, value):
        filter = queryset.filter
        queryset = filter(name__contains=value) or filter(lastname__contains=value) or filter(phonenumber__contains=value) or filter(cellphone__contains=value)
        return queryset

class ServicesFilter(django_filters.FilterSet):
    q = CharFilter(method='searchmethod',label="Αναζήτηση")

    class Meta:
        model = EspaService
        fields = []

    def searchmethod(self,queryset, name, value):
        filter = queryset.filter
        queryset = filter(service__contains=value)
        return queryset

class DocumentsBackendFilter(django_filters.FilterSet):
    q = CharFilter(method='searchmethod',label="Αναζήτηση")
    start_date = DateFilter(field_name="entrydate",lookup_expr="gte",label="Από")
    end_date = DateFilter(field_name="entrydate",lookup_expr="lte",label="Έως")

    class Meta:
        model = Document
        fields = []

    def searchmethod(self,queryset, name, value):
        filter = queryset.filter
        queryset = filter(name__contains=value) or filter(lastname__contains=value) or filter(phonenumber__contains=value) or filter(cellphone__contains=value)
        return queryset

class DocumentsFrontendFilter(django_filters.FilterSet):
    q = CharFilter(method='searchmethod',label="Αναζήτηση")
    start_date = DateFilter(field_name="entrydate",lookup_expr="gte",label="Από")
    end_date = DateFilter(field_name="entrydate",lookup_expr="lte",label="Έως")

    class Meta:
        model = Document
        fields = []

    def searchmethod(self,queryset, name, value):
        filter = queryset.filter
        queryset = filter(name__contains=value) or filter(lastname__contains=value) or filter(phonenumber__contains=value) or filter(cellphone__contains=value)
        return queryset