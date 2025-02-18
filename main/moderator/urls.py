from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_moderator_menu, name="moderator_menu"),
    path('login', views.show_login, name="moderator_login"),
    path('create', views.show_create, name="moderator_create"),
    path('employees/', views.show_employees, name="show_employees"),
    path('employees/<int:employee_id>/detail', views.show_employee_detail, name="employee_detail"),
    path('employees/<int:pk>/delete', views.EmployeeDeleteView.as_view(), name="employee_delete"),
    path('save_employees_to_file', views.save_employees_to_file, name="save_employees_to_file"),
    path('load_employees_from_file', views.load_employees_from_file, name="load_employees_from_file"),
    path('books/', views.show_books, name="show_books"),
    path('books/create', views.book_create, name="book_create"),
    path('books/<int:book_id>/detail', views.show_book_detail, name="book_detail"),
    path("books/<int:pk>/update", views.BookUpdateView.as_view(), name="book_update"),
    path('books/<int:pk>/delete', views.BookDeleteView.as_view(), name="book_delete"),
    path('save_books_to_file', views.save_books_to_file, name="save_books_to_file"),
    path('load_books_from_file', views.load_books_from_file, name="load_books_from_file"),
    path('sales/', views.show_sales, name="show_sales"),
    path('sales/create', views.sale_create, name="sale_create"),
    path('sales/<int:sale_id>/detail', views.show_sale_detail, name="sale_detail"),
    path("sales/<int:pk>/update", views.SaleUpdateView.as_view(), name="sale_update"),
    path('sales/<int:pk>/delete', views.SaleDeleteView.as_view(), name="sale_delete"),
    path('save_sales_to_file', views.save_sales_to_file, name="save_sales_to_file"),
    path('load_sales_from_file', views.load_sales_from_file, name="load_sales_from_file"),
    path('sales/sale_search_by_date/', views.search_sales_by_date, name="sale_search_by_date"),
    path('sales/sale_search_by_period/', views.search_sales_by_period, name="sale_search_by_period"),
    path('sales/sale_search_by_employee/', views.search_sales_by_employee, name="sale_search_by_employee"),
    path('book_search/', views.search_most_popular_book, name="book_search"),
    path('trader_search/', views.search_most_successful_trader, name="trader_search"),
    path('profit_calculation/', views.calculate_total_profit, name="calculate_profit"),
    path('author_search/', views.search_most_popular_author, name="author_search"),
    path('genre_search/', views.search_most_popular_genre, name="genre_search")
]
