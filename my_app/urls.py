from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.contracts_list, name='contracts_list'),
    re_path(r'^contracts/new/$', views.contract_new, name='contract_new'),
]
