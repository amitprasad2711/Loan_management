from django.db import models
from products.models import Product


class Customer(models.Model):

    EMPLOYMENT_CHOICES = [
        ("Salaried", "Salaried"),
        ("Self Employed", "Self Employed"),
    ]

    SALARY_TYPE_CHOICES = [
        ("Cash", "Cash"),
        ("Cheque", "Cheque"),
        ("DAT", "DAT"),
    ]

    STATUS_CHOICES = [
        ("Eligible", "Eligible"),
        ("Not Eligible", "Not Eligible"),
    ]

    full_name = models.CharField(max_length=150)

    age = models.PositiveIntegerField()

    monthly_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    employment_type = models.CharField(
        max_length=50,
        choices=EMPLOYMENT_CHOICES
    )

    salary_type = models.CharField(
        max_length=20,
        choices=SALARY_TYPE_CHOICES
    )

    credit_score = models.PositiveIntegerField()

    # eligibility_status = models.CharField(
    #     max_length=20,
    #     choices=STATUS_CHOICES,
    #     default="Not Eligible"
    # )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    

class EligibilityResult(models.Model):

    STATUS = [
        ("Eligible", "Eligible"),
        ("Not Eligible", "Not Eligible"),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS
    )

    reason = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.customer} - {self.product}"