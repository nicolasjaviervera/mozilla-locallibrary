from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def headercounters(request):
    num_instances_on_loan = BookInstance.objects.filter(status__exact='o').count()
    return {
        'num_instances_on_loan': num_instances_on_loan,
}