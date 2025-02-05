from django.shortcuts import render

# Create your views here.


def show_main_menu(request):
    return render(request, "employee/main_menu.html")


def show_library(request):
    return render(request, "employee/library.html")


def show_sales(request):
    return render(request, "employee/sales.html")
