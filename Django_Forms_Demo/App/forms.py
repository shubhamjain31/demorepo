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

    role = forms.CharField(error_messages={
        'required'              : 'Please Enter Role',
    },
    widget=forms.TextInput(
        attrs={
            "placeholder"       : "Role",
            "value"             : "",                
            "class"             : "form-control form-control-alternative"
        }
    ))

    class Meta:  
        model   = Employee 

        fields  = ['name', 'contact', 'email', 'role']

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name").title()
        return name

    def clean_role(self, *args, **kwargs):
        role = self.cleaned_data.get("role")
        if role == 'None':
            raise forms.ValidationError("Please Enter Role")
        else:
            return role