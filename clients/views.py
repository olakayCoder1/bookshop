from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Items , OrderItem, Order
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from django.views.generic import DetailView



def home_page(request):
    item1 = Items.objects.all()[:3]
    item2 = Items.objects.all()[3:7]

    your_cart = OrderItem.objects.filter(user_id=request.user, status='pending')
    total_cart_item = your_cart.aggregate(Sum('quantity'))['quantity__sum']

    orders = Order.objects.all()
    kb = Order.objects.filter(user_id=request.user)
    return render(request, 'clients/home.html', {'item1': item1,'item2': item2 , 'orders': orders , "kb":kb , 'your_cart': total_cart_item})



    
def about_item(request, id):
    item = get_object_or_404(Items, pk=id)
    your_cart = OrderItem.objects.filter(user_id=request.user, status='pending')
    total_cart_item = your_cart.aggregate(Sum('quantity'))['quantity__sum']
    return render(request, 'clients/about-item.html', {'item': item , 'your_cart': total_cart_item})


def all_product(request):
    items = Items.objects.all()
    your_cart = OrderItem.objects.filter(user_id=request.user, status='pending')
    total_cart_item = your_cart.aggregate(Sum('quantity'))['quantity__sum']

    return render(request, 'clients/all-products.html', {'items': items ,  'your_cart': total_cart_item})





def add_to_cart(request, id):
    item = get_object_or_404(Items, pk=id)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user_id=request.user,
        status='pending'
    )
    order_qs = Order.objects.filter(user_id=request.user, status='pending')
    if order_qs.exists():
        order = order_qs[0]
        print(order.item)
        # check if the order item is in the order
        if order.item.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("/")
        else:
            order.item.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("/")
    else:
        order = Order.objects.create(
            user_id=request.user)
        order.item.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("/")


def remove_single_item_from_cart(request, id):
    item = get_object_or_404(Items, pk=id)
    order_qs = Order.objects.filter(
        user_id=request.user,
        status='pending'
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.item.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user_id=request.user,
               status='pending'
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.item.remove(order_item)
                order_item.delete()
            return redirect("/")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("/about-item/"+str(id))
    else:
        messages.info(request, "You do not have an active order")
        return redirect('/')



def cart_detail(request):
    user = request.user
    items_in_cart = OrderItem.objects.filter(user_id=user, status="pending" )
    sum = 0
    for val in items_in_cart:
        sum += val.get_total_item_price()
    your_cart = OrderItem.objects.filter(user_id=request.user, status='pending')
    total_cart_item = your_cart.aggregate(Sum('quantity'))['quantity__sum']
    context = { 'items_in_cart' : items_in_cart , 'sum': sum , 'your_cart': total_cart_item}
    return render(request, 'clients/cart-details.html', context)



def search_item(request):
    search_word = request.GET['search']
    result = Items.objects.filter(name__icontains=search_word)
    your_cart = OrderItem.objects.filter(user_id=request.user, status='pending')
    total_cart_item = your_cart.aggregate(Sum('quantity'))['quantity__sum']
    return render(request, 'clients/search.html', {'results': result , 'your_cart': total_cart_item})

def check_out(request):
    if request.method == 'POST':
        user_address = request.POST['address']
        user_contact = request.POST['contact']
        
    items_in_cart = OrderItem.objects.filter(user_id=request.user, status="pending" )
    your_cart = OrderItem.objects.filter(user_id=request.user, status='pending')
    total_cart_item = your_cart.aggregate(Sum('quantity'))['quantity__sum']
    sum = 0
    for val in items_in_cart:
        sum += val.get_total_item_price()
    context = { 'items_in_cart' : items_in_cart , 'sum': sum , 'your_cart': total_cart_item}
    return render(request, 'clients/check-out.html' , context)