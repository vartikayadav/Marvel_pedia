from django.shortcuts import render,redirect
from Comics.models import Comics
from .models import Cart,CartItem
# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
def add_cart(request,product_id):
    product=Comics.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
        cart_id=_cart_id(request)
        )
        cart.save()
    try:
        cart_item=CartItem.objects.get(product=product,)    
