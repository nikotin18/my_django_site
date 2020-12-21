from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^clients/$', views.clients_list, name='clients_list'),
    re_path(r'^products/$', views.products_list, name='products_list'),
    re_path(r'^orders/$', views.orders_list, name='orders_list'),
    re_path(r'^clients/new/$', views.clients_new, name='clients_new'),
    re_path(r'^products/new/$', views.products_new, name='products_new'),
    re_path(r'^orders/new/$', views.orders_new, name='orders_new'),
]
