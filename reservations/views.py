from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import House, Order
from .forms import  OrderForm 
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def order_house(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.house = house

            existing_orders = Order.objects.filter(
                house=house,
                exit_date__gte=order.arrive_date,
                arrive_date__lte=order.exit_date
            )
            if existing_orders.exists():
                messages.error(request, 'در این تاریخ رزرو دیگری انجام شده است.')
                return redirect('house_detail', pk=pk)
            
            if order.count_of_passengers > house.capacity:
                messages.error(request, 'تعداد مسافران از ظرفیت خانه بیشتر است.')
                return redirect('house_detail', pk=pk)
            
            days = (order.exit_date - order.arrive_date).days
            if days <= 0:
                messages.error(request, 'تاریخ خروج باید بعد از تاریخ ورود باشد.')
                return redirect('house_detail', pk=pk)

            order.total_price = house.price_per_day * days
            order.save()
            messages.success(request, 'رزرو خانه با موفقیت انجام شد.')
            return redirect('house_detail', pk=pk)  
    else:
        form = OrderForm()
    return render(request, 'house/house_detail.html', {'form': form, 'house': house})


@login_required
def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    houses = House.objects.all()
    if request.method == 'POST':
        order.delete()
        return redirect('user_orders')
    return render(request, 'reservations/confirm_cancel_order.html', {'order': order,'houses': houses})


@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'reservations/user_orders.html', {'orders': orders})


@login_required
def host_reservations(request):
    if request.user.role != 2: 
        return redirect('home')
    houses = House.objects.filter(user=request.user)
    reservations = Order.objects.filter(house__in=houses)
    return render(request, 'reservations/host_reservations.html', {'reservations': reservations})
