from ..models import Receipt,Expense
from Millennium_System import settings
def receiptSumToday():
    today_receipts = Receipt.objects.all().filter(entrydate=settings.CURRENT_DATE)
    sum = 0
    for i in today_receipts:
        sum += i.amount
    return sum

def expenseSumToday():
    today_expenses = Expense.objects.all().filter(entrydate=settings.CURRENT_DATE)
    sum = 0
    for i in today_expenses:
        sum += i.amount
    return sum