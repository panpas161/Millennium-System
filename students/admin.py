from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Specialty)
admin.site.register(Installment)
admin.site.register(Voucher)
admin.site.register(Department)
admin.site.register(StudentSpecialty)