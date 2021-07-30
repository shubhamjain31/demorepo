from django.shortcuts import render
from django.http import HttpResponse

from Django_Relationships.decorators import *
from App.models import *

from django.db.models import Prefetch

# Create your views here.

# --------------------------------------------------@ select_related @-----------------------------------------------

@query_debugger
def book_list(request):
    
    queryset = Book.objects.all()
    
    books = []
    for book in queryset:
        books.append({'id': book.id, 'name': book.name, 'price':book.price, 'publisher': book.publisher.name})
        
    return render(request, 'index.html', {'books':books})

@query_debugger
def book_list_select_related(request):

    queryset = Book.objects.select_related('publisher').all()

    books = []

    for book in queryset:
        books.append({'id': book.id, 'name': book.name, 'price':book.price, 'publisher': book.publisher.name})

    return render(request, 'index.html', {'books':books})


# --------------------------------------------------@ prefetch_related @-----------------------------------------------

@query_debugger
def store_list(request):

    queryset = Store.objects.all()

    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})

    return render(request, 'index.html', {'stores':stores})

@query_debugger
def store_list_prefetch_related(request):
  
    queryset = Store.objects.prefetch_related('books')

    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})

    return render(request, 'index.html', {'stores':stores})

@query_debugger
def store_list_expensive_books_prefetch_related(request):
  
    queryset = Store.objects.prefetch_related('books')

    stores = []
    for store in queryset:
        books = [book.name for book in store.books.filter(price__range=(1000, 5000))]
        stores.append({'id': store.id, 'name': store.name, 'books': books})

    return render(request, 'index.html', {'stores':stores})

@query_debugger
def store_list_expensive_books_prefetch_related_efficient(request):

    queryset = Store.objects.prefetch_related(
        Prefetch('books', queryset=Book.objects.filter(price__range=(1000, 5000))))

    stores = []
    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})

    return render(request, 'index.html', {'stores':stores})


# --------------------------------------------------@ One-to-one @-----------------------------------------------

@query_debugger
def person_list(request):
    queryset = Adhar.objects.select_related('person').all()

    persons = []
    for person in queryset:
        persons.append({"id":person.id, "name":person.person.name, "email":person.person.email, "mobile":person.person.mobile, "signature":person.signature,
                        "adhar":person.adhar_no})

    return render(request, 'index.html', {'persons':persons})
