from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from books.models import Book
from mysite.forms import ContactForm

import time
import sys
import datetime
import logging


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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd.get('email', 'noreply@example.com'),
            #     ['siteowner@example.com'],
            # )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!', 'message': u'django'})
    return render(request, 'contact_form.html', {'form': form})


def thanks(request):
    return HttpResponse('thanks')


def sell(request, item, price, quantity):
    return render(request, 'sell.html', {'quantity': quantity, 'item': item, 'price': price})


def object_list(request, model, template_name=None):
    obj_list = model.objects.all()
    if template_name is None:
        template_name = '%s_list.html' % model.__name__.lower()
    return render(request, template_name, {'object_list': obj_list})


def day_archive(request, year='2017', month='01', day='01'):
    # The following statement raises a TypeError!
    date = datetime.date(int(year), int(month), int(day))
    return render(request, 'temps_list.html', {'title': sys._getframe().f_code.co_name, 'date': date})


def method_splitter(request, GET=None, POST=None):
    logging.debug("A log message")
    if request.method == 'GET' and GET is not None:
        logging.debug("A log message")
        return GET(request)
    elif request.method == 'POST' and POST is not None:
        logging.debug("A log message")
        return POST(request)
    raise Http404


def some_page_get(request):
    assert request.method == 'GET'
    return HttpResponse('get')


@csrf_protect
def some_page_post(request):
    assert request.method == 'POST'
    logging.debug("A log message")
    return render(request, 'meta.html', {})
    # return HttpResponseRedirect('/contact/thanks')
