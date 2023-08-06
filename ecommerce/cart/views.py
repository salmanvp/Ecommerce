from django.shortcuts import render, redirect
from shop.models import Product
from .models import Cart, Account, Order
from django.contrib.auth.decorators import login_required

@login_required
def addcart(request, p):
    p = Product.objects.get(slug=p)
    user = request.user
    try:
        cart = Cart.objects.get(user=user, product=p)
        if (cart.quantity < cart.product.stock):
            cart.quantity += 1
            cart.save()
    except Cart.DoesNotExist:

        cart = Cart.objects.create(user=user, product=p, quantity=1)
        cart.save()

    return redirect('cart:cartview')

@login_required
def cartview(request):
    total = 0
    user = request.user
    try:
        cart = Cart.objects.filter(user=user)
        for i in cart:
            total = i.quantity * i.product.price
    except Cart.DoesNotExist:
        pass
    return render(request, 'cart.html', {'cart': cart, 'total': total})


@login_required
def cart_remove(request, p):
    p = Product.objects.get(slug=p)
    user = request.user
    try:
        cart = Cart.objects.get(user=user, product=p)
        if (cart.quantity > 1):
            cart.quantity -= 1
            cart.save()
        else:
            cart.delete()
    except Cart.DoesNotExist:
        pass
    return redirect('cart:cartview')


@login_required
def cart_delete(request, p):
    p = Product.objects.get(slug=p)
    user = request.user
    try:
        cart = Cart.objects.get(user=user, product=p)
        cart.delete()
    except Cart.DoesNotExist:
        pass
    return redirect('cart:cartview')

@login_required
def orderform(request):
    total = 0
    if (request.method == "POST"):
        address = request.POST['address']
        phone = request.POST['phoneNo']
        acctno = request.POST['AcNo']
        user = request.user
        cart = Cart.objects.filter(user=user)
        for i in cart:
            total += i.quantity * i.product.price
        try:
            ac = Account.objects.get(acctnumber=acctno)
            if (ac.amount >= total):
                ac.amount = ac.amount - total
                ac.save()
                for i in cart:
                    a = Order.objects.create(user=user, product=i.product, address=address, phone=phone, order_status="paid",
                                            no_of_items=i.quantity)
                    a.save()
                    i.product.stock = i.product.stock - i.quantity
                    i.product.save()
                cart.delete()
                msg = "Order placed successfully"
                return render(request, 'orderdetails.html', {'msg': msg})
            else:
                msg = "Insufficient Amount.Cannot place this order"
                return render(request, 'orderdetails.html', {'msg': msg})
        except Account.DoesNotExist:
            msg = "Account number is not valid"
            return render(request, 'orderform.html', {'msg': msg})


    return render(request, 'orderform.html', )

@login_required(login_url='shop.user_login')
def orderview(request):
    u=request.user
    o=Order.objects.filter(user=u,order_status="paid")
    return render(request,'orderview.html',{'o':o,'u':u.username})
