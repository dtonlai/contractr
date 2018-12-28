from django.shortcuts import render
from django.views.generic import (TemplateView)
from django.http import HttpResponseRedirect, HttpResponse

class ContractrIndexView(TemplateView):
    template_name = 'index.html'
