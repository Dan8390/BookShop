from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_employee_menu, name="employee_menu"),
    path('account', views.show_account, name="account"),
    path('library', views.show_library, name="library"),
    path('sales', views.show_sales, name="sales"),
    path('login', views.show_login, name="login"),
    path('create', views.show_create, name="create")
]
