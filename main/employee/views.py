from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Book, Sale
from .forms import EmployeeForm
from django.views.generic import UpdateView
import hashlib

# Create your views here.


class EmployeeUpdateView(UpdateView):
    model = Employee
    success_url = "../.."
    template_name = "employee/employee_update.html"
    form_class = EmployeeForm


def compute_sha512_hash(input_string):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(input_string.encode('utf-8'))
    return sha512_hash.hexdigest()


def show_employee_menu(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, "employee/employee_menu.html", {'employee': employee})


def show_account(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, "employee/account.html", {'employee': employee})


def show_library(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    books = Book.objects.all()
    return render(request, "employee/library.html", {'books': books, 'employee': employee})


def show_sales(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    sales = Sale.objects.all()
    employee_sales = []
    for sale in sales:
        if sale.employee.id == employee_id:
            employee_sales.append(sale)
    return render(request, "employee/sales.html", {'employee_sales': employee_sales, 'employee': employee})


def show_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        hash_password = compute_sha512_hash(password)
        try:
            employee = Employee.objects.get(email=email, password=hash_password)
            return redirect("employee_menu", employee_id=employee.id)
        except:
            return render(request, "employee/login.html")

    return render(request, "employee/login.html")


def show_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.password = str(compute_sha512_hash(employee.password))
            employee.save()
            return redirect("login")

    form = EmployeeForm
    data = {"form": form}
    return render(request, "employee/create_employee.html", data)
