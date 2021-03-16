from .models import Student,Teacher,Specialty
import django_filters
from django_filters import CharFilter,DateFilter

class StudentFilter(django_filters.FilterSet):
    q = CharFilter(method='searchmethod',label="Αναζήτηση")
    start_date = DateFilter(field_name="entrydate",lookup_expr="gte",label="Από")
    end_date = DateFilter(field_name="entrydate",lookup_expr="lte",label="Έως")

    def searchmethod(self,queryset, name, value):
        filter = queryset.filter
        queryset = filter(name__contains=value) or filter(lastname__contains=value) or filter(phonenumber__contains=value) or filter(cellphone__contains=value)
        return queryset

class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = "__all__"

class SpecialtyFilter(django_filters.FilterSet):
    class Meta:
        model = Specialty
        fields = "__all__"