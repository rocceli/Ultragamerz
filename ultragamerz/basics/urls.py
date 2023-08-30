from django.urls import path
from . import views
from .views import SearchResultsView,verification_View
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("register",views.Register,name="register"),
    path('login', views.Login, name='login'),
    path('contact', views.Contact_Us, name='contact'),
    path("",views.home,name="home"),
    path('logout', views.Logout, name='logout'),
    path('products', views.Products.as_view(), name='products'),
    path('activate/<uidb64>/<token>',verification_View.as_view(),name='activate'),
    path('search/', csrf_exempt(SearchResultsView.as_view()), name='search'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]
