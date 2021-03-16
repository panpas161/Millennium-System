from django_filters import CharFilter
import django_filters

class UserFilter(django_filters.FilterSet):
     q = CharFilter(method='searchMethod')

     def searchMethod(self,queryset,name,value):
         filter = queryset.filter
         queryset = filter(username__contains=value) or filter(first_name__contains=value) or filter(
             last_name__contains=value) or filter(email__contains=value)
         return queryset