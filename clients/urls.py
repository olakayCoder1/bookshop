from django.urls import path
from .import views






urlpatterns = [ 
    path('', views.home_page, name='home-page'),
    path('products/', views.all_product, name='products'),
    path('about-item/<str:id>', views.about_item, name='about-item'),
    path('add-to-cart/<str:id>', views.add_to_cart, name='add-to-cart'),
    path('cart-details/', views.cart_detail, name='cart-details'),
    path('delete-from-cart/<str:id>', views.remove_single_item_from_cart, name='delete-from-cart'),
    

]