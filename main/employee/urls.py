from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_main_menu, name="main_menu"),
    path('library', views.show_library, name="library"),
    path('sales', views.show_sales, name="sales")
]
