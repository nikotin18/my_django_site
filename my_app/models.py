from django.db import models
from django.utils import timezone


# заказчик
class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.PositiveBigIntegerField()

    def __str__(self):
        return "%s, %s" % (self.first_name, self.last_name)


# товар
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name


# договор
class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_of_conclude = models.DateField() # дата заключения
    date_of_execute = models.DateField(null=True, blank=True) # дата выполнения

    def conclude(self):
        self.date_of_conclude = timezone.now()
        self.save()

    def execute(self):
        self.date_of_execute = timezone.now()
        self.save()

    def __str__(self):
        return "%s %s, %s: %i шт." % (self.client.first_name, self.client.last_name,
                                      self.product.name, self.quantity)
