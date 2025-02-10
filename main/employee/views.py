from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Create your views here.


def show_employee_menu(request):
    return render(request, "employee/employee_menu.html")


def show_account(request):
    return render(request, "employee/account.html")


def show_library(request):
    return render(request, "employee/library.html")


def show_sales(request):
    return render(request, "employee/sales.html")


def show_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            employee = Employee.objects.get(email=email, password=password)
            return redirect("employee_menu", employee_id=employee.id)
        except:
            return render(request, "employee/login.html")

    return render(request, "employee/login.html")


def show_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    form = EmployeeForm
    data = {"form": form}
    return render(request, "employee/create_employee.html", data)
