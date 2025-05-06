"""
URL configuration for textile_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from textile_app.views import home, manufacturers, suppliers, retailers, place_order, payment
from textile_app import views  # Make sure this line exists

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Home page URL
    path("manufacturers/", manufacturers, name="manufacturers"),
    path('suppliers/', suppliers, name='suppliers'),  # Ensure this line exists
    path("retailers/", retailers, name="retailers"),
    path("place_order/",place_order, name="place_order"),
    path("payment/<int:order_id>/",payment, name="payment"),
    path('captcha/', include('captcha.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forget-password/', views.forget_password_view, name='forget_password'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
]



