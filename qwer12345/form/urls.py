from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='form-index'),
    path('forms/', views.forms, name='form-forms'),
]
