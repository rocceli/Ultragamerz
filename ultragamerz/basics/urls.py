from django.urls import path
from . import views

urlpatterns = [
    path("register",views.Register,name="register"),
    path('login', views.Login, name='login'),
    path('contact', views.Contact_Us, name='contact'),
    path("",views.home,name="home"),
    path('logout', views.Logout, name='logout'),
    path('products', views.Products.as_view(), name='products'),
]

