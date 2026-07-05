from django.db import models

class Product(models.Model):

    EMPLOYMENT_CHOICES = [
        ('Salaried', 'Salaried'),
        ('Self Employed', 'Self Employed'),
    ]

    SALARY_TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('DAT', 'DAT'),
    ]

    loan_name = models.CharField(max_length=100)
    min_age = models.PositiveIntegerField()
    max_age = models.PositiveIntegerField()
    min_credit_score = models.PositiveIntegerField()

    # Abhi simple CharField rakhenge.
    # Baad me multi-select karenge.
    employment_type = models.CharField(
        max_length=50,
        choices=EMPLOYMENT_CHOICES
    )

    salary_type = models.CharField(
        max_length=20,
        choices=SALARY_TYPE_CHOICES
    )

    min_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.loan_name