from django.contrib import admin
from .models import Employee, Book, Sale

# Register your models here.

admin.site.register(Employee)
admin.site.register(Book)
admin.site.register(Sale)
