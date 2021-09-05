from django import forms  
from App.models import Employee  


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(required=False,
    widget=forms.TextInput(
        attrs={
            "placeholder"       : "Name",
            "value"             : "",                
            "class"             : "form-control form-control-alternative"
        }
    ))

    email = forms.EmailField(error_messages={
        'required'              : 'Please Enter Email',
    },
        widget=forms.EmailInput(
            attrs={
                "placeholder"   : "Email",                
                "class"         : "form-control form-control-alternative"
            }
        ))

    contact = forms.CharField(required=False,
    widget=forms.TextInput(
        attrs={
            "placeholder"       : "Contact",
            "value"             : "",                
            "class"             : "form-control form-control-alternative"
        }
    ))

    class Meta:  
        model   = Employee 

        fields  = ['name', 'contact', 'email']

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name").title()
        return name