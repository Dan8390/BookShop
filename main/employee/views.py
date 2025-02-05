from django.shortcuts import render

# Create your views here.


def show_main_menu(request):
    return render(request, "user/main_menu.html")
