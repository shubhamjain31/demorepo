from django.shortcuts import render
from django.http import HttpResponse

from Django_Relationships.decorators import *
from App.models import *

# Create your views here.

# --------------------------------------------------@ select_related @-----------------------------------------------

@query_debugger
def book_list(request):
    
    queryset = Book.objects.all()
    
    books = []
    for book in queryset:
        books.append({'id': book.id, 'name': book.name, 'publisher': book.publisher.name})
        
    return render(request, 'index.html', {'books':books})

@query_debugger
def book_list_select_related(request):

    queryset = Book.objects.select_related('publisher').all()

    books = []

    for book in queryset:
        books.append({'id': book.id, 'name': book.name, 'publisher': book.publisher.name})

    return render(request, 'index.html', {'books':books})

# --------------------------------------------------@ prefetch_related @-----------------------------------------------
