# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def search_form(request):
    return render_to_response('search_form.html')
