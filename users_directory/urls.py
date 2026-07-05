from django.urls import path
from . import views

urlpatterns = [
    path("",views.customer_list,name="customer_list"),

    path("add/",views.add_customer,name="add_customer"),
    path("report/<int:pk>/",views.customer_report,name="customer_report",),
    path("edit/<int:pk>/",views.edit_customer,name="edit_customer",),
    path("delete/<int:pk>/",views.delete_customer,name="delete_customer"),
]