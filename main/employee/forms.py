from .models import Employee
from django.forms import ModelForm, TextInput


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['surname', 'name', 'middle_name', 'position', 'contact_phone', 'email', 'password']
        widgets = {
            'surname': TextInput(attrs={
                'class': 'form-control'
            }),
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'middle_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'position': TextInput(attrs={
                'class': 'form-control'
            }),
            'contact_phone': TextInput(attrs={
                'class': 'form-control'
            }),
            'email': TextInput(attrs={
                'class': 'form-control'
            }),
            'password': TextInput(attrs={
                'class': 'form-control'
            })
        }
