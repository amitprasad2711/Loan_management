from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm
from .utils import evaluate_customer
from .models import EligibilityResult
from django.db.models import Q

def customer_list(request):
    customers = Customer.objects.all().order_by("-id")

    return render(
        request,
        "users_directory/customer_list.html",
        {
            "customers": customers
        }
    )


def add_customer(request):

    if request.method == "POST":

        form = CustomerForm(request.POST)

        if form.is_valid():

            customer = form.save()

            evaluate_customer(customer)

            return redirect("customer_list")

    else:

        form = CustomerForm()

    return render(
        request,
        "users_directory/customer_form.html",
        {
            "form": form
        }
    )


def customer_report(request, pk):

    customer = Customer.objects.get(id=pk)

    eligible_products = EligibilityResult.objects.filter(
        customer=customer,
        status="Eligible"
    )

    not_eligible_products = EligibilityResult.objects.filter(
        customer=customer,
        status="Not Eligible"
    )

    return render(
        request,
        "users_directory/customer_report.html",
        {
            "customer": customer,
            "eligible_products": eligible_products,
            "not_eligible_products": not_eligible_products,
        }
    )


def edit_customer(request, pk):

    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":

        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():

            customer = form.save()

            # Puri eligibility dobara calculate hogi
            evaluate_customer(customer)

            return redirect("customer_list")

    else:

        form = CustomerForm(instance=customer)

    return render(
        request,
        "users_directory/customer_form.html",
        {
            "form": form
        }
    )


def delete_customer(request, pk):

    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        customer.delete()
        return redirect("customer_list")

    return render(
        request,
        "users_directory/delete_customer.html",
        {
            "customer": customer
        }
    )



def customer_list(request):

    query = request.GET.get("q","")

    customers = Customer.objects.all().order_by("-id")

    if query:
        customers = customers.filter(
            Q(full_name__icontains=query)
        )

    return render(
        request,
        "users_directory/customer_list.html",
        {
            "customers": customers,
            "query": query
        }
    )