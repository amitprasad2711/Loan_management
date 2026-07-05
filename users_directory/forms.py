from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer

        fields = [
            "full_name",
            "age",
            "monthly_salary",
            "employment_type",
            "salary_type",
            "credit_score",
            # "eligibility_status"
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "monthly_salary": forms.NumberInput(attrs={"class": "form-control"}),
            "employment_type": forms.Select(attrs={"class": "form-select"}),
            "salary_type": forms.Select(attrs={"class": "form-select"}),
            "credit_score": forms.NumberInput(attrs={"class": "form-control"}),
            # "eligibility_status": forms.Select(attrs={"class": "form-select"}),
        }