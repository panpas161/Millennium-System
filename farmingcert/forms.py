from .models import Farmer
from django.forms import ModelForm

class FarmerModelForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(FarmerModelForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Farmer
        fields = "__all__"