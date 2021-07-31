from django.urls import path
from . import views
#추가
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.StoreView.as_view(), name="store"),
    #path('', views.store, name="store"),
    path('cart/', views.CartView.as_view(), name="cart"),
    #path('cart/', views.cart, name="cart"),
    #path('checkout/', views.CheckoutView.as_view(), name="checkout"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updatedItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    #추가
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="store/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name="product_detail"),
    path('add-product/', views.ProductAddView.as_view(), name="add_product"),
]
