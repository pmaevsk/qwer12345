from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import MyForm
import json
from django.core import serializers


def forms(request):
    if request.method == 'POST':
        data = request.POST
        data_json = {"form": []}
        try:
            for i in range(0, 99):
                field = "name{}".format(i)
                print(data[field])
                if (data[field]):
                    data_json['form'].append({field: data[field]})
                else:
                    pass
            if data_json["form"] == []:
                pass
            else:
                MyForm.objects.create(metadata=data_json)
        except:
            if data_json["form"] == []:
                pass
            else:
                MyForm.objects.create(metadata=data_json)
    context = {}
    return render(request, 'form/forms.html', context)


def my_forms(request):
    my_forms = MyForm.objects.all()
    tmpJson = serializers.serialize("json", my_forms)
    my_forms = json.loads(tmpJson)
    return render(request, 'form/submforms.html', {'my_forms': my_forms})


def index(request):
    return HttpResponse('<a class="button" href="/forms">Submit form</a>''<br>'
                        '<a class="button" href="/my_forms">List my submitted forms</a>''<br>')
