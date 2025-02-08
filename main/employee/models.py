from django.db import models

# Create your models here.


class Employee(models.Model):
    surname = models.CharField("Прізвище", max_length=25)
    name = models.CharField("Ім'я", max_length=25)
    middle_name = models.CharField("По батькові", max_length=30)
    position = models.CharField("Посвдв", max_length=30)
    contact_phone = models.CharField("Контактний телефон", max_length=19)
    email = models.CharField("Електронна пошта", max_length=60)
    password = models.CharField("Пароль", max_length=30)
    profit = models.IntegerField("Прибуток")

    def __str__(self):
        return self.email


class Book(models.Model):
    title = models.CharField("Назва", max_length=30)
    year_of_publication = models.IntegerField("Рік публікації")
    author = models.CharField("Автор", max_length=40)
    genre = models.CharField("Жанр", max_length=35)
    cost = models.IntegerField("Собівартість")
    potential_selling_price = models.IntegerField("Потенційна ціна продажу")

    def __str__(self):
        return self.title


class Sales(models.Model):
    employee = models.CharField("Співробітник", max_length=80)
    book = models.CharField("Книга", max_length=30)
    date = models.DateField("Дата продажу")
    real_selling_price = models.IntegerField("Реальна ціна продажу")

    def __str__(self):
        return self.employee
