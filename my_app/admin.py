from django.contrib import admin
from .models import Client
from .models import Product
from .models import Contract

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Contract)
