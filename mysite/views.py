from django.http import HttpResponse, Http404
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
# from mysite.books.models import Book
import time

def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    # assert False

    next_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', locals())


def display_meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response('meta.html', locals())

# def book_list(request):
#     books = Book.objects.order_by('name')
#     return render_to_response('book_list.html', {'books': books})

