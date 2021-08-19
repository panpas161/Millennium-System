from django.urls import path
from .views import *

urlpatterns =[
    #receipts
    path('receipts/list/',listReceiptsView,name="list_receipts"),
    path('receipts/add',addReceiptView,name="add_receipt"),
    path('receipts/edit/<str:pk>',editReceiptView,name="edit_receipt"),
    path('receipts/delete/<str:pk>',deleteReceiptView,name="delete_receipt"),
    #expenses
    path('expenses/list',listExpensesView,name="list_expenses"),
    path('expenses/add', addExpenseView,name="add_expense"),
    path('expenses/edit/<str:pk>',editExpenseView,name="edit_expense"),
    path('expenses/delete/<str:pk>',deleteExpenseView,name="delete_expense"),
    #register
    path('overview',registerOverviewView,name="register_overview"),
    path('overview/get_logistics/<app>/<date>',getRevenue,name="get_logistics"),
]