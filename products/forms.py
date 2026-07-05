from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            "loan_name",
            "min_age",
            "max_age",
            "min_credit_score",
            "employment_type",
            "salary_type",
            "min_salary",
        ]

        widgets = {

            "loan_name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "min_age": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "max_age": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "min_credit_score": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "employment_type": forms.Select(attrs={
                "class": "form-select"
            }),

            "salary_type": forms.Select(attrs={
                "class": "form-select"
            }),

            "min_salary": forms.NumberInput(attrs={
                "class": "form-control"
            }),
        }