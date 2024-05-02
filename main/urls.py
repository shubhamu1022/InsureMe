from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('maid-insurance/', views.maid_insurance, name='maid_insurance'),
    path('accident-insurance/', views.accident_insurance, name='accident_insurance'),
    path('travel-insurance/', views.travel_insurance, name='travel_insurance'),
    path('recommend/', views.recommend_policy, name='recommend-policy'),
    path('products/accident/', views.products_accident, name='products_accident'),
    path('products/maid/', views.products_maid, name='products_maid'),
    path('products/travel/', views.products_travel, name='products_travel'),
    path('products/checkout', views.checkout, name = 'checkout'),
    path('products/cart', views.cart, name = 'cart'),
]