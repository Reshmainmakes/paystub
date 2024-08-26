# invoices/forms.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name', 'position', 'regular_hour_rate', 'overtime_hour_rate',
            'week1_regular_hours', 'week1_overtime_hours',
            'week2_regular_hours', 'week2_overtime_hours',
            'week3_regular_hours', 'week3_overtime_hours',
            'week4_regular_hours', 'week4_overtime_hours'
        ]
        name = forms.CharField(required=True)
        position = forms.CharField(required=True)