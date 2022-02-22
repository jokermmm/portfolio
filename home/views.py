from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Data
def landing_page(request):
    person = Data.objects.all()[0]
    return render(request, "home/html1.html" , {'name': person.name, 'title': person.title, 'education': person.education})