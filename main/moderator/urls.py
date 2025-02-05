from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_moderator_menu, name="moderator_menu")
]
