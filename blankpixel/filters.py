import django_filters
from django_filters import CharFilter,DateFilter,ModelChoiceFilter
from .models import *

class ClientFilter(django_filters.FilterSet):
    q = CharFilter(method='searchMethod',label="Αναζήτηση")
    # start_date = DateFilter(field_name="entrydate",lookup_expr="gte",label="Από")
    # end_date = DateFilter(field_name="entrydate",lookup_expr="lte",label="Έως")
    # services = ModelChoiceFilter(queryset=Service.objects.all())
    class Meta:
        model = Client
        fields = []

    def searchMethod(self, queryset, name, value):
        filter = queryset.filter
        queryset = filter(firstname__contains=value) or filter(lastname__contains=value) or filter(companyname__contains=value) \
        or filter(companytype__contains=value) or filter(phonenumber__contains=value)
        return queryset

class ServiceFilter(django_filters.FilterSet):
    q = CharFilter(method='searchMethod',label="Αναζήτηση")

    class Meta:
        model = Service
        fields = []
    def searchMethod(self,queryset,name,value):
        filter = queryset.filter
        queryset = filter(firstname__contains=value)
        return queryset

class InstallmentFilter(django_filters.FilterSet):
    q = CharFilter(method='searchMethod',label="Αναζήτηση")

    class Meta:
        model = Installment
        fields =[]

    def searchMethod(self,queryset,name,value):
        filter = queryset.filter
        queryset = filter(price__contains=value)
        return queryset