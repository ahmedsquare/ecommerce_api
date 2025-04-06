# orders/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm

# View to list all orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

# View to create a new order
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')  # Redirect to the order list view after successful creation
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

# View to display a single order
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})
