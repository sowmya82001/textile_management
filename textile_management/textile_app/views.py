from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Manufacturer, Supplier, Retailer, Order, Payment

from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from django.contrib.auth.models import User
from .models import OTPStorage
from django.core.mail import send_mail
import random
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Order
from django.http import HttpResponse

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

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Use the new form with CAPTCHA
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials or CAPTCHA, please try again.")
    else:
        form = LoginForm()  # Use the new form with CAPTCHA

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def forget_password_view(request):
    if request.method == 'POST':
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                otp = str(random.randint(100000, 999999))
                OTPStorage.objects.update_or_create(user=user, defaults={'otp': otp})
                send_mail(
                    'Your OTP Code',
                    f'Your OTP code is {otp}',
                    'admin@example.com',
                    [email],
                    fail_silently=False,
                )
                request.session['reset_email'] = email
                return redirect('reset_password')
            except User.DoesNotExist:
                form.add_error('email', 'Email not found.')
    else:
        form = ForgetPasswordForm()
    return render(request, 'forget_password.html', {'form': form})

def reset_password_view(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            new_password = form.cleaned_data['new_password']
            email = request.session.get('reset_email')
            if email:
                try:
                    user = User.objects.get(email=email)
                    otp_obj = OTPStorage.objects.get(user=user)
                    if otp_obj.otp == otp:
                        user.set_password(new_password)
                        user.save()
                        otp_obj.delete()
                        return redirect('login')
                    else:
                        form.add_error('otp', 'Invalid OTP')
                except (User.DoesNotExist, OTPStorage.DoesNotExist):
                    form.add_error('otp', 'Invalid attempt')
            else:
                form.add_error(None, 'Session expired, try again')
    else:
        form = ResetPasswordForm()
    return render(request, 'reset_password.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return redirect('/')