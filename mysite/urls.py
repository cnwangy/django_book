"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import mysite.views
import books.views
import books.models

urlpatterns = [
    url(r'^$', mysite.views.hello),
    url(r'^hello/$', mysite.views.hello),
    url('^time/$', mysite.views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', mysite.views.hours_ahead),
    url(r'^disp/$', mysite.views.display_meta),

    url(r'^search/$', books.views.search),
    url(r'^contact/$', mysite.views.contact),
    url(r'^contact/thanks/$', mysite.views.thanks),
    url(r'^admin/', admin.site.urls),

    url(r'^mydata/birthday/$', mysite.views.sell, {'item': 'jan', 'price': 6, 'quantity': 21}),
    url(r'^mydata/(?P<item>\w+)/(?P<price>\d+)/(?P<quantity>\d+)/$', mysite.views.sell),

    url(r'^events/$', mysite.views.object_list, {'model': books.models.Author}),
    url(r'^blog/entries/$', mysite.views.object_list, {'model': books.models.Book}),
    url(r'^temps/$', mysite.views.object_list, {'model': books.models.Author, 'template_name': 'temps_list.html'}),
    url(r'^articles/(\d{4})/(\d{1,2})/(\d{1,2})/$', mysite.views.day_archive),
    url(r'^search/somepage$', mysite.views.method_splitter,
        {'GET': mysite.views.some_page_get, 'POST': mysite.views.some_page_post}),

]
