from django.shortcuts import render, redirect, get_object_or_404
from employee.models import Employee, Book, Sale
from django.views.generic import DeleteView, UpdateView
import json
from django.http import HttpResponse
from employee.forms import EmployeeForm
from employee.views import compute_sha512_hash
from .forms import BookForm
from datetime import date

# Create your views here.


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '..'
    template_name = 'moderator/employee_delete.html'


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "moderator/book_update.html"
    success_url = ".."


class BookDeleteView(DeleteView):
    model = Book
    success_url = '..'
    template_name = 'moderator/book_delete.html'


class SaleUpdateView(UpdateView):
    model = Sale
    template_name = "moderator/sale_update.html"
    success_url = ".."


class SaleDeleteView(DeleteView):
    model = Sale
    success_url = '..'
    template_name = 'moderator/sale_delete.html'


def show_moderator_menu(request):
    return render(request, "moderator/moderator_menu.html")


def show_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        hash_password = compute_sha512_hash(password)
        try:
            employee = Employee.objects.get(email=email, password=hash_password)
            if str(employee.email).startswith("moderator"):
                return redirect("moderator_menu")
            else:
                return render(request, "employee/employee_menu.html")
        except:
            return render(request, "moderator/moderator_login.html")

    return render(request, "moderator/moderator_login.html")


def show_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.password = str(compute_sha512_hash(employee.password))
            employee.save()
            if employee.email.startswith("moderator"):
                return redirect("moderator_login")
            else:
                return render(request, "employee/employee_login.html")

    form = EmployeeForm
    data = {"form": form}
    return render(request, "moderator/moderator_create.html", data)


def show_employees(request):
    employees = Employee.objects.all()
    employees_to_show = []
    for employee in employees:
        if not employee.email.startswith('moderator'):
            employees_to_show.append(employee)
    return render(request, "moderator/employees.html", {'employees': employees_to_show})


def show_employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, "moderator/employee_detail_view.html", {'employee': employee})


def save_employees_to_file(request):
    employees = Employee.objects.all()

    employees_data = {
        'employees': [{
            'surname': employee.surname,
            'name': employee.name,
            'middle_name': employee.middle_name,
            'position': employee.position,
            'contact_phone': employee.contact_phone,
            'email': employee.email,
            'password': employee.password
        } for employee in employees]
    }

    with open('employees.json', 'w') as file:
        json.dump(employees_data, file, indent=4)
    return render(request, 'moderator/save_employees_to_file.html')


def load_employees_from_file(request):
    try:
        with open('employees.json', 'r') as file:
            employees_data = json.load(file)
            for employee in employees_data.get('employees'):
                Employee.objects.get_or_create(surname=employee['surname'], name=employee['name'],
                                               middle_name=employee['middle_name'], position=employee['position'],
                                               contact_phone=employee['contact_phone'], email=employee['email'],
                                               password=employee['password'])
            return render(request, "moderator/load_employees_from_file.html")
    except FileNotFoundError:
        return HttpResponse('<h4>Помилка імпорту файлу. Файл не знайдено</4>')
    except json.JSONDecodeError:
        return HttpResponse('<h4>Помилка імпорту файлу. JSON не може розшифруватися</4>')


def show_books(request):
    books = Book.objects.all()
    return render(request, "moderator/books.html", {'books': books})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('..')
    form = BookForm()
    data = {'form': form}
    return render(request, 'moderator/book_create.html', data)


def show_book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "moderator/book_detail_view.html", {'book': book})


def save_books_to_file(request):
    books = Book.objects.all()

    books_data = {
        'books': [{
            'title': book.title,
            'year_of_publication': book.year_of_publication,
            'author': book.author,
            'genre': book.genre,
            'cost': book.cost,
            'potential_selling_price': book.potential_selling_price
        } for book in books]
    }

    with open('books.json', 'w') as file:
        json.dump(books_data, file, indent=4)
    return render(request, 'moderator/save_books_to_file.html')


def load_books_from_file(request):
    try:
        with open('books.json', 'r') as file:
            books_data = json.load(file)
            for book in books_data.get('books'):
                Book.objects.get_or_create(title=book['title'], year_of_publication=book['year_of_publication'],
                                           author=book['author'], genre=book['genre'], cost=book['cost'],
                                           potential_selling_price=book['potential_selling_price'])
            return render(request, "moderator/load_books_from_file.html")
    except FileNotFoundError:
        return HttpResponse('<h4>Помилка імпорту файлу. Файл не знайдено</4>')
    except json.JSONDecodeError:
        return HttpResponse('<h4>Помилка імпорту файлу. JSON не може розшифруватися</4>')


def show_sales(request):
    sales = Sale.objects.all()
    return render(request, "moderator/sales.html", {'sales': sales})


# def sale_create(request):
#     if request.method == 'POST':
#         form = SaleForm(request.POST)
#         if form.is_valid():
#             sale = form.save(commit=False)
#             sale.employee = Employee.objects.get_or_create(surname=sale.surname, name=sale.name,
#                                                            middle_name=sale.middle_name, position=sale.position,
#                                                            contact_phone=sale.contact_phone, email=sale.email,
#                                                            password=sale.password)
#             sale.book = Book.objects.get_or_create(title=sale.title, year_of_publication=sale.year_of_publication,
#                                                    author=sale.author, genre=sale.genre, cost=sale.cost,
#                                                    potential_selling_price=sale.potential_selling_price)
#             sale.save()
#             return redirect('..')
#     form = SaleForm()
#     data = {'form': form}
#     return render(request, 'moderator/sale_create.html', data)
#

def show_sale_detail(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    return render(request, "moderator/sale_detail_view.html", {'sale': sale})


def save_sales_to_file(request):
    sales = Sale.objects.all()

    sales_data = {
        'sales': [{
            'employee': {
                'surname': sale.employee.surname,
                'name': sale.employee.name,
                'middle_name': sale.employee.middle_name,
                'position': sale.employee.position,
                'contact_phone': sale.employee.contact_phone,
                'email': sale.employee.email,
                'password': sale.employee.password
            },
            'book': {
                'title': sale.book.title,
                'year_of_publication': sale.book.year_of_publication,
                'author': sale.book.author,
                'genre': sale.book.genre,
                'cost': sale.book.cost,
                'potential_selling_price': sale.book.potential_selling_price
            },
            'date': str(sale.date),
            'real_selling_price': sale.real_selling_price
        } for sale in sales]
    }

    with open('sales.json', 'w') as file:
        json.dump(sales_data, file, indent=4)
    return render(request, 'moderator/save_sales_to_file.html')


def load_sales_from_file(request):
    try:
        with open('sales.json', 'r') as file:
            sales_data = json.load(file)
            for sale in sales_data.get('sales'):
                Sale.objects.get_or_create(employee=Employee.objects.get_or_create(surname=sale['employee']['surname'],
                                           name=sale['employee']['name'], middle_name=sale['employee']['middle_name'],
                                           position=sale['employee']['position'],
                                           contact_phone=sale['employee']['contact_phone'],
                                           email=sale['employee']['email'], password=sale['employee']['password']),
                                           book=Book.objects.get_or_create(title=sale['book']['title'],
                                           year_of_publication=sale['book']['year_of_publication'],
                                           author=sale['book']['author'], genre=sale['book']['genre'],
                                           cost=sale['book']['cost'],
                                           potential_selling_price=sale['book']['potential_selling_price']),
                                           date=sale['date'], real_selling_price=sale['real_selling_price'])
            return render(request, "moderator/load_sales_from_file.html")
    except FileNotFoundError:
        return HttpResponse('<h4>Помилка імпорту файлу. Файл не знайдено</4>')
    except json.JSONDecodeError:
        return HttpResponse('<h4>Помилка імпорту файлу. JSON не може розшифруватися</4>')


def search_sales_by_date(request):
    if request.method == "POST":
        sale_date = request.POST.get('date')
        sales = Sale.objects.all()
        sales_to_show = []
        for sale in sales:
            split_date = str(sale.date).split('-')
            if sale_date == date(int(split_date[0]), int(split_date[1]), int(split_date[2])).isoformat():
                sales_to_show.append(sale)
        return render(request, "moderator/sales_by_date.html", {"sales": sales_to_show})
    return render(request, "moderator/sale_search_by_date.html")


def search_sales_by_employee(request):
    if request.method == "POST":
        employee = request.POST.get('email')
        sales = Sale.objects.all()
        sales_to_show = []
        for sale in sales:
            if sale.employee.email == employee:
                sales_to_show.append(sale)
        return render(request, "moderator/sales_by_employee.html", {"sales": sales_to_show})
    return render(request, "moderator/sale_search_by_employee.html")


def search_sales_by_period(request):
    if request.method == "POST":
        start = request.POST.get('start')
        end = request.POST.get('end')
        sales = Sale.objects.all()
        sales_to_show = []
        for sale in sales:
            split_date = str(sale.date).split('-')
            if start < date(int(split_date[0]), int(split_date[1]), int(split_date[2])).isoformat() < end:
                sales_to_show.append(sale)
        return render(request, "moderator/sales_by_period.html", {"sales": sales_to_show})
    return render(request, "moderator/sale_search_by_period.html")


def search_most_popular_book(request):
    if request.method == "POST":
        start = request.POST.get('start')
        end = request.POST.get('end')
        books = Book.objects.all()
        books_list = []
        books_dict = {}
        for book in books:
            books_list.append(book.title)
            books_dict[book.title] = 0
        sales = Sale.objects.all()
        period_sales = []
        for sale in sales:
            split_date = str(sale.date).split('-')
            if start < date(int(split_date[0]), int(split_date[1]), int(split_date[2])).isoformat() < end:
                period_sales.append(sale)
        for sale in period_sales:
            books_dict[sale.book.title] += 1
        for i in range(len(books_list)-1):
            for j in range(len(books_list)-i-1):
                if books_dict[books_list[j]] > books_dict[books_list[j+1]]:
                    buffer = books_list[j]
                    books_list[j] = books_list[j+1]
                    books_list[j+1] = buffer

        most_popular_book = books_list[len(books_list)-1]
        return render(request, "moderator/most_popular_book.html", {"book": most_popular_book})
    return render(request, "moderator/most_popular_book_search.html")


def search_most_successful_trader(request):
    if request.method == "POST":
        start = request.POST.get('start')
        end = request.POST.get('end')
        traders_list = []
        traders_dict = {}
        sales = Sale.objects.all()
        period_sales = []
        for sale in sales:
            split_date = str(sale.date).split('-')
            if start < date(int(split_date[0]), int(split_date[1]), int(split_date[2])).isoformat() < end:
                period_sales.append(sale)
        for sale in period_sales:
            traders_list.append(sale.employee)
            traders_dict[sale.employee] = 0
        for sale in period_sales:
            traders_dict[sale.employee] += sale.real_selling_price - sale.book.potential_selling_price
        for i in range(len(traders_list) - 1):
            for j in range(len(traders_list) - i - 1):
                if traders_dict[traders_list[j]] > traders_dict[traders_list[j + 1]]:
                    buffer = traders_list[j]
                    traders_list[j] = traders_list[j + 1]
                    traders_list[j + 1] = buffer
        most_successful_trader = traders_list[len(traders_list)-1]
        return render(request, "moderator/most_successful_trader.html", {'trader': most_successful_trader})
    return render(request, "moderator/most_successful_trader_search.html")


def calculate_total_profit(request):
    if request.method == "POST":
        start = request.POST.get('start')
        end = request.POST.get('end')
        sales = Sale.objects.all()
        period_sales = []
        for sale in sales:
            split_date = str(sale.date).split('-')
            if start < date(int(split_date[0]), int(split_date[1]), int(split_date[2])).isoformat() < end:
                period_sales.append(sale)
        total_profit = 0
        for sale in period_sales:
            total_profit += (sale.real_selling_price - sale.book.potential_selling_price)
        return render(request, "moderator/total_profit.html", {'profit': total_profit})
    return render(request, "moderator/calculate_total_profit.html")


def search_most_popular_author(request):
    if request.method == "POST":
        start = request.POST.get('start')
        end = request.POST.get('end')
        books = Book.objects.all()
        authors_list = []
        authors_dict = {}
        for book in books:
            authors_list.append(book.author)
            authors_dict[book.author] = 0
        sales = Sale.objects.all()
        period_sales = []
        for sale in sales:
            split_date = str(sale.date).split('-')
            if start < date(int(split_date[0]), int(split_date[1]), int(split_date[2])).isoformat() < end:
                period_sales.append(sale)
        for sale in period_sales:
            authors_dict[sale.book.author] += 1
        for i in range(len(authors_list) - 1):
            for j in range(len(authors_list) - i - 1):
                if authors_dict[authors_list[j]] > authors_dict[authors_list[j + 1]]:
                    buffer = authors_list[j]
                    authors_list[j] = authors_list[j + 1]
                    authors_list[j + 1] = buffer

        most_popular_author = authors_list[len(authors_list) - 1]
        return render(request, "moderator/most_popular_author.html", {"author": most_popular_author})
    return render(request, "moderator/most_popular_author_search.html")


def search_most_popular_genre(request):
    if request.method == "POST":
        start = request.POST.get('start')
        end = request.POST.get('end')
        books = Book.objects.all()
        genres_list = []
        genres_dict = {}
        for book in books:
            genres_list.append(book.genre)
            genres_dict[book.genre] = 0
        sales = Sale.objects.all()
        period_sales = []
        for sale in sales:
            split_date = str(sale.date).split('-')
            if start < date(int(split_date[0]), int(split_date[1]), int(split_date[2])).isoformat() < end:
                period_sales.append(sale)
        for sale in period_sales:
            genres_dict[sale.book.genre] += 1
        for i in range(len(genres_list) - 1):
            for j in range(len(genres_list) - i - 1):
                if genres_dict[genres_list[j]] > genres_dict[genres_list[j + 1]]:
                    buffer = genres_list[j]
                    genres_list[j] = genres_list[j + 1]
                    genres_list[j + 1] = buffer

        most_popular_genre = genres_list[len(genres_list) - 1]
        return render(request, "moderator/most_popular_genre.html", {"genre": most_popular_genre})
    return render(request, "moderator/most_popular_genre_search.html")
