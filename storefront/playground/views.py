import collections
from os import name
from turtle import title
from typing import Collection
from django.shortcuts import render
from django.db import transaction, connection
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.db.models import Value, Q, F, Func, Count, ExpressionWrapper, DecimalField  #Q is represent for query or a code that reproduces a value, F can reference to particular fields
from store.models import Product, OrderItem, Order, Customer, Collection
from tags.models import TaggedItem

#request -> response !!!!
#request and return response
# Action (views)
# in view we can pull data from database, transform data, send email etc.


def say_hello (request):  
    
    
    return render(request, 'hello.html', { 'name': 'Azka'})
