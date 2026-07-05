from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from products.models import Product
from users_directory.models import Customer, EligibilityResult


@login_required(login_url="login")
def dashboard(request):

    context = {

        "total_products": Product.objects.count(),

        "total_customers": Customer.objects.count(),

        "eligible_count": EligibilityResult.objects.filter(
            status="Eligible"
        ).count(),

        "not_eligible_count": EligibilityResult.objects.filter(
            status="Not Eligible"
        ).count(),

        "recent_customers": Customer.objects.order_by("-id")[:5],

        "recent_products": Product.objects.order_by("-id")[:5],

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )