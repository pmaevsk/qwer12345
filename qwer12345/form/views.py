from django.shortcuts import render
from django.http import HttpResponse


def forms(request):
    return render(request, 'form/forms.html')


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
