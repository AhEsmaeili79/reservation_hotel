from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from house.models import House
from reservations.models import Order

User = get_user_model()

@login_required
def admin_panel(request):
    if not request.user.is_superuser:
        return redirect('home')

    context = {
        'users': User.objects.all(),
        'houses': House.objects.all(),
        'orders': Order.objects.all(),
        'host_requests': User.objects.filter(role_change_requested=True),
    }

    if request.method == 'POST':
        action_type = request.POST.get('action_type')

        if action_type == 'add_admin':
            new_admin_username = request.POST.get('new_admin_username')
            try:
                new_admin = User.objects.get(username=new_admin_username)
                new_admin.is_staff = True
                new_admin.save()
                messages.success(request, 'کاربر به عنوان مدیر افزوده شد.')
            except User.DoesNotExist:
                messages.error(request, 'کاربری با این نام کاربری وجود ندارد.')

        elif action_type == 'delete_user':
            user_id = request.POST.get('user_id')
            user = get_object_or_404(User, id=user_id)
            user.delete()
            messages.success(request, 'کاربر با موفقیت حذف شد.')

        elif action_type == 'delete_house':
            house_id = request.POST.get('house_id')
            house = get_object_or_404(House, id=house_id)
            house.delete()
            messages.success(request, 'خانه با موفقیت حذف شد.')

        elif action_type == 'delete_order':
            order_id = request.POST.get('order_id')
            order = get_object_or_404(Order, id=order_id)
            order.delete()
            messages.success(request, 'سفارش با موفقیت حذف شد.')

        elif action_type == 'toggle_user_status':
            user_id = request.POST.get('user_id')
            user = get_object_or_404(User, id=user_id)
            user.is_active = not user.is_active
            user.save()
            messages.success(request, f'کاربر {"فعال" if user.is_active else "غیرفعال"} شد.')

        elif action_type == 'toggle_house_status':
            house_id = request.POST.get('house_id')
            house = get_object_or_404(House, id=house_id)
            house.is_active = not house.is_active
            house.save()
            messages.success(request, f'خانه {"فعال" if house.is_active else "غیرفعال"} شد.')

        elif action_type == 'handle_host_request':
            user_id = request.POST.get('user_id')
            approve = request.POST.get('approve') == 'true'
            user = get_object_or_404(User, id=user_id)
            if approve:
                user.role = 2
            user.role_change_requested = False
            user.save()
            messages.success(request, 'درخواست تغییر نقش کاربر پردازش شد.')

        return redirect('admin_panel')  # All actions will redirect to the admin panel

    return render(request, 'admin/admin_panel.html', context)

def host_houses(request):
    if request.user.is_authenticated and request.user.role == 2:
        host_houses = House.objects.filter(user=request.user)
        return render(request, 'admin/host_houses.html', {'host_houses': host_houses})
    else:
        return render(request, 'admin/access_denied.html')  

@login_required
def admin_delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'کاربر با موفقیت حذف شد.')
    return redirect('admin_panel')  # Redirect to the admin panel after deleting a user


@login_required
def admin_delete_house(request, house_id):
    house = get_object_or_404(House, id=house_id)
    house.delete()
    messages.success(request, 'خانه با موفقیت حذف شد.')
    return redirect('admin_panel')  # Redirect to the admin panel after deleting a house


@login_required
def admin_delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    messages.success(request, 'سفارش با موفقیت حذف شد.')
    return redirect('admin_panel')  # Redirect to the admin panel after deleting an order


@login_required
def toggle_user_status(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_active = not user.is_active
    user.save()
    messages.success(request, f'کاربر {"فعال" if user.is_active else "غیرفعال"} شد.')
    return redirect('admin_panel')  # Redirect to the admin panel after toggling user status


@login_required
def toggle_house_status(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    house.is_active = not house.is_active
    house.save()
    messages.success(request, f'خانه {"فعال" if house.is_active else "غیرفعال"} شد.')
    return redirect('admin_panel')  # Redirect to the admin panel after toggling house status


def host_requests(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        user = get_object_or_404(User, id=user_id)
        if action == 'approve':
            user.role = 2
        user.role_change_requested = False
        user.save()
        return redirect('host_requests')

    users_requesting_role_change = User.objects.filter(role_change_requested=True)
    return render(request, 'admin/admin_panel.html', {'users': users_requesting_role_change})