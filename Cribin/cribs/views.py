# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Crib

# Create your views here.
def index(request):

    cribs = Crib.objects.all() #Ignore it
    latest_cribs = cribs.order_by('-number_of_rooms')[:5] #Ajouter système de matching ici
    context = {'latest_cribs' : latest_cribs}
    #output = ','.join([c.address for c in latest_cribs])
    return render(request, 'cribs/browse.html', context)








def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)