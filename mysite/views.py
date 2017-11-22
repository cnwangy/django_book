from django.http import HttpResponse, Http404
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from mysite.forms import ContactForm

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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!','message':u'django'})
    return render_to_response('contact_form.html', {'form': form})