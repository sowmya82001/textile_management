from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("manufacturers/", views.manufacturers, name="manufacturers"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path("retailers/", views.retailers, name="retailers"),
    path("place_order/", views.place_order, name="place_order"),
    path("payment/<int:order_id>/", views.payment, name="payment"),
]
