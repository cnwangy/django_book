from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")


def home(request):
    return HttpResponse("This is home")


def current_datetime(request):
    current_date = datetime.datetime.now()
    name = 'wang'
    return render_to_response('current_datetime.html', locals())

def hours_ahead(request,of,mins):
    try:
        hours = int(of)
        minutes = int(mins)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hours,minutes=minutes)
    return render_to_response('hours_ahead.html', locals())
