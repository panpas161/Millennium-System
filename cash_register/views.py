from django.shortcuts import render
from .forms import ReceiptModelForm,ExpenseModelForm
from .models import Receipt,Expense
from django.shortcuts import redirect
from django.contrib import messages
from .functions import receipts
from assets.decorators.decorators import staff_only
from django.contrib.auth.decorators import login_required
from assets.functions.pagination import getPage
from .filters import *

#receipts
@login_required(login_url="login")
@staff_only
def listReceiptsView(request):
    objects = Receipt.objects.all().order_by("-id")
    page = getPage(request,objects,ReceiptFilter)
    data = {
        'objects':page
    }
    return render(request,"Backend/Receipts/list_receipts.html",data)

@login_required(login_url="login")
@staff_only
def addReceiptView(request):
    form = ReceiptModelForm()
    recipient = request.user.last_name + " " + request.user.first_name
    client = request.GET.get('client')
    if client is None:
        client = ""
    data = {
        'form': form,
        'recipient':recipient,
        'client':client
    }
    if request.method == "POST":
        form = ReceiptModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Η απόδειξη προστέθηκε επιτυχώς!")
            return redirect("list_receipts")
    return render(request,"Backend/Receipts/add_receipt.html",data)

@login_required(login_url="login")
@staff_only
def editReceiptView(request,pk):
    forminstance = Receipt.objects.get(id=pk)
    form = ReceiptModelForm(instance=forminstance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = ReceiptModelForm(request.POST,instance=forminstance)
        if form.is_valid():
            form.save()
            messages.success("Η απόδειξη άλλαξε με επιτυχία!")
            return redirect("list_receipts")
    return render(request,"Backend/Receipts/edit_receipt.html",data)

@login_required(login_url="login")
@staff_only
def deleteReceiptView(request,pk):
    instance = Receipt.objects.get(id=pk)
    instance.delete()
    messages.success(request,"Η απόδειξη διαγράφτηκε με επιτυχία!")
    return redirect("list_receipts")

@login_required(login_url="login")
@staff_only
def printReceiptView(request,pk):
    instance = Receipt.objects.get(id=pk)
    data = {
        'instance':instance
    }
    return render(request,"Backend/Receipts/print_receipt.html",data)

#expenses
@login_required(login_url="login")
@staff_only
def listExpensesView(request):
    expenses = Expense.objects.all().order_by("-id")
    page = getPage(request,expenses,ExpenseFilter)
    data = {
        'expenses':page
    }
    return render(request,"Backend/Expenses/list_expenses.html",data)

@login_required(login_url="login")
@staff_only
def addExpenseView(request):
    form = ExpenseModelForm()
    data = {
        'form':form
    }
    if request.method == "POST":
        form = ExpenseModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Τα έξοδα προστέθηκαν επιτυχώς!")
            return redirect("list_expenses")
    return render(request,"Backend/Expenses/add_expense.html",data)

@login_required(login_url="login")
@staff_only
def editExpenseView(request,pk):
    forminstance = Expense.objects.get(id=pk)
    form = ExpenseModelForm(instance=forminstance)
    data = {
        'form':form
    }
    if request.method == "POST":
        form = ExpenseModelForm(request.POST,instance=forminstance)
        if form.is_valid():
            form.save()
            messages.success("Τα έξοδα άλλαξαν με επιτυχία!")
            return redirect("list_expenses")
    return render(request,"Backend/Expenses/edit_expense.html",data)

@login_required(login_url="login")
@staff_only
def deleteExpenseView(request,pk):
    instance = Expense.objects.get(id=pk)
    data = {
        'object':instance
    }
    if request.method == "POST":
        instance.delete()
        messages.sucess(request,"Τα προεπιλεγμένα έξοδα διαγράφτηκαν επιτυχώς!")
        return redirect("list_expenses")
    return render(request,"Backend/Expenses/delete_expense",data)

#register
@login_required(login_url="login")
@staff_only
def registerOverviewView(request):
    data = {
        'todayreceiptsamount':receipts.receiptSumToday(),
        'todayexpenseamount':receipts.expenseSumToday(),
        'todaytotalrevenue':receipts.receiptSumToday() - receipts.expenseSumToday()
    }

    return render(request,"Backend/Register/register_overview.html",data)