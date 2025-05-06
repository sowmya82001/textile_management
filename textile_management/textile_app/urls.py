from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("manufacturers/", views.manufacturers, name="manufacturers"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path("retailers/", views.retailers, name="retailers"),
    path("place_order/", views.place_order, name="place_order"),
    path("payment/<int:order_id>/", views.payment, name="payment"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forget-password/', views.forget_password_view, name='forget_password'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
]
