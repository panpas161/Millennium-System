from django.forms.models import ModelForm
from .models import efetStudent,efetBusiness

class EfetStudentModelForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(EfetStudentModelForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = efetStudent
        fields = "__all__"

class EfetBusinessModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EfetBusinessModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = efetBusiness
        fields = "__all__"