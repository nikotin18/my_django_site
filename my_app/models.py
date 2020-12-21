from django.db import models
from django.utils import timezone


# заказчик
class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return "%s, %s" % (self.first_name, self.last_name)


# товар
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stored = models.IntegerField() # в наличии на складе

    def __str__(self):
        return self.name


# заказ
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField() # количество товара
    date = models.DateField() # дата покупки

    def complete(self): # выполнить заказ
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return "%s: %s %s, %s - %i шт." % (self.date, self.client.first_name, self.client.last_name,
                                      self.product.name, self.quantity)
