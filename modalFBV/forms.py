from django import forms
from .models import Projects, Employees


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = "__all__"
        widgets = {
            'pr_name': forms.TextInput(attrs={'class': 'form-control', 'size': '150'}),
            'pr_number': forms.TextInput(attrs={'class': 'fomr-control', 'size': '20'}),
            'pr_address': forms.TextInput(attrs={'class': 'form-control', 'size': '255'}),
            'pr_meeting_url': forms.TextInput(attrs={'class': 'form-control', 'size': '255'}),
            'pr_parking_url': forms.TextInput(attrs={'class': 'form-control', 'size': '255'}),
        }
