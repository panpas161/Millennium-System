from django.forms import ModelForm
from .models import Receipt,Expense
from django import forms
from Millennium_System import settings
from assets.functions.ids import getReceiptNextID,getExpenseNextID

class ReceiptModelForm(ModelForm):
    class Meta:
        model = Receipt
        fields = '__all__'
        widgets = {
            'date':forms.DateInput(format=settings.DATE_FORMAT)
        }

class ExpenseModelForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'date':forms.DateInput(format=settings.DATE_FORMAT)
        }