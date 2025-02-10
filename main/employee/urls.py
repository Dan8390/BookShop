from django.urls import path
from . import views

urlpatterns = [
    path('<int:employee_id>/', views.show_employee_menu, name="employee_menu"),
    path('<int:employee_id>/account', views.show_account, name="account"),
    path('<int:employee_id>/library/', views.show_library, name="library"),
    path('<int:employee_id>/sales', views.show_sales, name="sales"),
    path('login', views.show_login, name="login"),
    path('create', views.show_create, name="create"),
    path('<int:pk>/employee_update', views.EmployeeUpdateView.as_view(), name="employee_update")
]
