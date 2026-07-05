from .models import EligibilityResult
from products.models import Product


def evaluate_customer(customer):
    # Purane results delete kar do
    # print("Evaluate Called For :", customer.full_name)
    EligibilityResult.objects.filter(customer=customer).delete()

    products = Product.objects.all()

    for product in products:
        reasons = []

        # Age Check
        if customer.age < product.min_age:
            reasons.append(f"Minimum age required is {product.min_age}")

        if customer.age > product.max_age:
            reasons.append(f"Maximum age allowed is {product.max_age}")

        # Salary Check
        if customer.monthly_salary < product.min_salary:
            reasons.append(f"Minimum salary required is {product.min_salary}")

        # Credit Score Check
        if customer.credit_score < product.min_credit_score:
            reasons.append(f"Minimum credit score required is {product.min_credit_score}")

        # Employment Type
        if customer.employment_type != product.employment_type:
            reasons.append("Employment type does not match")

        # Salary Type
        if customer.salary_type != product.salary_type:
            reasons.append("Salary type does not match")

        # Save Result
        # Save Result
        if reasons:

            # print("--------------------------------")
            # print("Customer :", customer.full_name)
            # print("Product :", product.loan_name)
            # print("Reasons :", reasons)

            EligibilityResult.objects.create(
                customer=customer,
                product=product,
                status="Not Eligible",
                reason="\n".join(reasons)
            )

        else:

            print("--------------------------------")
            print("Customer :", customer.full_name)
            print("Product :", product.loan_name)
            print("Eligible")

            EligibilityResult.objects.create(
                customer=customer,
                product=product,
                status="Eligible",
                reason=""
            )