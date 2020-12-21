from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Client, Order
from .forms import ProductForm, ClientForm, OrderForm
from django.utils import timezone
from django.shortcuts import redirect
from django.db.models import Sum

def index(request):
    return render(request, 'my_app/index.html', {})

def orders_list(request):
    orders = Order.objects.order_by('date')

    table = ""
    for order in orders:
        table += """<tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%i</td>
                        <td>%s</td>
        </tr>""" % (order.client, order.product, order.quantity, order.date)
    return render(request, 'my_app/orders.html', {'table': table})

def clients_list(request):
    clients = Client.objects.order_by('last_name')

    table = ""
    for client in clients:
        table += """<tr>
                        <td>%s %s %s</td>
                        <td>%i</td>
        </tr>""" % (client.last_name, client.first_name, client.middle_name if client.middle_name else "", client.phone_number)
    return render(request, 'my_app/clients.html', {'table': table})

def products_list(request):
    products_sold = Order.objects.values('product_id').annotate(the_sum=Sum('quantity'))
    products = Product.objects.order_by('id')

    total = 0
    for product_sold in products_sold:
        total += products[product_sold['product_id']-1].price * product_sold['the_sum']

    table = ""
    for product in products:
        table += """<tr>
            <td>%s</td>
            <td>%s</td>
            <td>%i</td>
        </tr>""" % (product.name, product.price, product.stored)

    return render(request, 'my_app/products.html', {'table': table, 'total': total})

def clients_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)

        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('clients_list')
    else:
        form = ClientForm()
        return render(request, 'my_app/clients_new.html', {'form': form})

def products_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('products_list')
    else:
        form = ProductForm()
        return render(request, 'my_app/products_new.html', {'form': form})

def orders_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('orders_list')
    else:
        form = OrderForm()
        return render(request, 'my_app/orders_new.html', {'form': form})
