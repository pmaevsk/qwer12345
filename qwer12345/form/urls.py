from django.urls import path
from django.contrib import admin
from form import views
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='form-index'),
    path('forms/', views.forms, name='form-forms'),
    path('my_forms/', views.my_forms, name='form-my_forms')
]
