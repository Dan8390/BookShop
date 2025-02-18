from django.forms import ModelForm, TextInput, NumberInput, DateInput
from employee.models import Book, Sale


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'year_of_publication', 'author', 'genre', 'cost', 'potential_selling_price']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control'
            }),
            'year_of_publication': NumberInput(attrs={
                'class': 'form-control'
            }),
            'author': TextInput(attrs={
                'class': 'form-control'
            }),
            'genre': TextInput(attrs={
                'class': 'form-control'
            }),
            'cost': NumberInput(attrs={
                'class': 'form-control'
            }),
            'potential_selling_price': NumberInput(attrs={
                'class': 'form-control'
            })
        }


# class SaleForm(ModelForm):
#     class Meta:
#         model = Sale
#         fields = ['employee', 'book', 'date', 'real_selling_price']
#         widgets = {
#             'employee': ForeignKey(attrs={
#                 'class': 'form-control'
#             }),
#             'book': ForeignKey(attrs={
#                 'class': 'form-control'
#             }),
#             'date': DateInput(attrs={
#                 'class': 'form-control'
#             }),
#             'real_selling_price': NumberInput(attrs={
#                 'class': 'form-control'
#             })
#         }
