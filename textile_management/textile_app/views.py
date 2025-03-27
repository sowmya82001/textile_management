from django.shortcuts import render, redirect
from .models import Manufacturer, Supplier, Retailer, Order, Payment

def home(request):
    return render(request, "home.html")

def manufacturers(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, "manufacturers.html", {"manufacturers": manufacturers})

def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, "suppliers.html", {"suppliers": suppliers})

def retailers(request):
    retailers_list = Retailer.objects.all()
    return render(request, "retailers.html", {"retailers": retailers_list})

def place_order(request):
    if request.method == "POST":
        retailer_id = request.POST["retailer"]
        product_name = request.POST["product_name"]
        quantity = request.POST["quantity"]
        order = Order.objects.create(retailer_id=retailer_id, product_name=product_name, quantity=quantity)
        return redirect("payment", order_id=order.id)
    retailers = Retailer.objects.all()
    return render(request, "place_order.html", {"retailers": retailers})

def payment(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == "POST":
        amount = request.POST["amount"]
        Payment.objects.create(order=order, amount=amount, status="Paid")
        order.status = "Completed"
        order.save()
        return redirect("home")
    return render(request, "payment.html", {"order": order})
