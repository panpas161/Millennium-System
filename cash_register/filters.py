from django_filters import CharFilter,DateFilter
import django_filters
from .models import Expense,Receipt

class ReceiptFilter(django_filters.FilterSet):
    q = CharFilter(method='searchmethod',label="Αναζήτηση")
    start_date = DateFilter(field_name="date",lookup_expr="gte",label="Από")
    end_date = DateFilter(field_name="date",lookup_expr="lte",label="Έως")
    def searchmethod(self,queryset,name,value):
        filter = queryset.filter
        queryset = filter(customer__contains=value) or filter(reason__contains=value) or filter(ammount_contains=value)
        return queryset
    class Meta:
        model = Receipt
        fields = ['paymentmethod','paymentway']
class ExpenseFilter(django_filters.FilterSet):
    q = CharFilter(method='searchmethod',label="Αναζήτηση")
    start_date = DateFilter(field_name="date",lookup_expr="gte",label="Από")
    end_date = DateFilter(field_name="date",lookup_expr="lte",label="Έως")
    def searchmethod(self,queryset,name,value):
        filter = queryset.filter
        queryset = filter(accountable__contains=value) or filter(recipient__contains=value) or filter(reason__contains=value)
        return queryset
    class Meta:
        model = Expense
        fields = ['category','paymentmethod','type','paymentway']