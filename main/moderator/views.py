from django.shortcuts import render

# Create your views here.


def show_moderator_menu(request):
    return render(request, "moderator/main_menu.html")
