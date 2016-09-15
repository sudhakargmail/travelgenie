# -*- coding: utf-8 -*-


from __future__ import unicode_literals


from django.shortcuts import render

from django.http import HttpResponse
from travelgenie import main
import json

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def searchflight(request):
	return HttpResponse(main.amadeus_flight_search_webhook(request.body))