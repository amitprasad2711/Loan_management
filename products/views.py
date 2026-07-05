from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.shortcuts import get_object_or_404
from users_directory.models import Customer
from users_directory.utils import evaluate_customer
from django.http import HttpResponseForbidden

def product_list(request):

    products = Product.objects.all()

    return render(
        request,
        "products/product_list.html",
        {
            "products": products
        }
    )


def add_product(request):

    if not request.user.is_superuser:
        return HttpResponseForbidden("Permission Denied")

    if request.method == "POST":

        form = ProductForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("product_list")

    else:

        form = ProductForm()

    return render(
        request,
        "products/product_form.html",
        {
            "form": form
        }
    )


def edit_product(request, pk):

    if not request.user.is_superuser:
        return HttpResponseForbidden("Permission Denied")

    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":

        form = ProductForm(request.POST, instance=product)

        if form.is_valid():

            # Product update
            form.save()

            # Sabhi customers ki eligibility dobara calculate karo
            customers = Customer.objects.all()

            for customer in customers:
                evaluate_customer(customer)

            return redirect("product_list")

    else:
        form = ProductForm(instance=product)

    return render(
        request,
        "products/product_form.html",
        {
            "form": form
        }
    )

def delete_product(request, pk):

    if not request.user.is_superuser:
        return HttpResponseForbidden("Permission Denied")
    
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(request, "products/delete_product.html", {
        "product": product
    })

from django.db.models import Q

def product_list(request):

    query = request.GET.get("q")

    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(loan_name__icontains=query)
        )

    return render(
        request,
        "products/product_list.html",
        {
            "products": products,
            "query": query
        }
    )
