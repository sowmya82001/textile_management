from django.db import models
from django.contrib.auth.models import User

class OTPStorage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    
from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Retailer(models.Model):
    name = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=[("Pending", "Pending"), ("Completed", "Completed")], default="Pending")

    def __str__(self):
        return f"Order {self.id} - {self.product_name}"

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[("Pending", "Pending"), ("Paid", "Paid")], default="Pending")

    def __str__(self):
        return f"Payment for Order {self.order.id}"
