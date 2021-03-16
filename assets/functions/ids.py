from cash_register.models import Receipt,Expense
def getReceiptNextID():
    next_id = Receipt.objects.order_by("-id").first()
    if next_id is None:
        next_id = 0
    else:
        next_id = Receipt.objects.all().order_by("-id").first().id + 1
    return next_id

def getExpenseNextID():
    next_id = Expense.objects.order_by("-id").first()
    if next_id is None:
        next_id = 0
    else:
        next_id = Expense.objects.all().order_by("-id").first().id + 1
    return next_id

#The above are to be deleted keep only the below

def getModelNextID(model):
    next_id =  model.objects.order_by("-id").first()
    if next_id is None:
        next_id = 0
    else:
        next_id = model.objects.all().order_by("-id").first().id + 1
    return next_id