from django.shortcuts import render


def show_welcome_page(request):
    return render(request, "main/welcome_page.html")
