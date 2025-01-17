from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import get_user_model
from house.models import House
from reservations.models import Order

User = get_user_model()


@login_required
def admin_panel(request):
    if not request.user.is_superuser:
        return redirect('home')  

    return render(request, 'admin/admin_panel.html')


@login_required
def admin_users_list(request):
    if not request.user.is_superuser:
        return redirect('home')  

    users = User.objects.all()
    return render(request, 'admin/admin_users_list.html', {'users': users})


@login_required
def admin_houses_list(request):
    if not request.user.is_superuser:
        return redirect('home')  

    houses = House.objects.all()
    return render(request, 'admin/admin_houses_list.html', {'houses': houses})


# @login_required
# def admin_add_house(request):
#     if not request.user.is_superuser:
#         return redirect('home')  

#     # Handle adding house form submission
#     return render(request, 'admin/admin_add_house.html')


@login_required
def admin_orders_list(request):
    if not request.user.is_superuser:
        return redirect('home')  

    orders = Order.objects.all()
    return render(request, 'admin/admin_orders_list.html', {'orders': orders})


@login_required
def admin_add_admin(request):
    if not request.user.is_superuser:
        return redirect('home')  

    if request.method == 'POST':
        new_admin_username = request.POST.get('new_admin_username')
        try:
            new_admin = User.objects.get(username=new_admin_username)
            new_admin.is_staff = True
            new_admin.save()
            messages.success(request, 'کاربر به عنوان مدیر افزوده شد.')
        except User.DoesNotExist:
            messages.error(request, 'کاربری با این نام کاربری وجود ندارد.')

    return redirect('admin_panel')


def admin_required(user):
    return user.is_authenticated and user.role == 1


@user_passes_test(admin_required)
def admin_users_list(request):
    users = User.objects.all()
    return render(request, 'admin/admin_users_list.html', {'users': users})


@user_passes_test(admin_required)
def admin_houses_list(request):
    houses = House.objects.all()
    return render(request, 'admin/admin_houses_list.html', {'houses': houses})


@user_passes_test(admin_required)
def admin_orders_list(request):
    orders = Order.objects.all()
    return render(request, 'admin/admin_orders_list.html', {'orders': orders})


@user_passes_test(lambda u: u.role == 1)  
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
    return render(request, 'admin/host_requests.html', {'users': users_requesting_role_change})


def host_houses(request):
    if request.user.is_authenticated and request.user.role == 2:
        host_houses = House.objects.filter(user=request.user)
        return render(request, 'admin/host_houses.html', {'host_houses': host_houses})
    else:
        return render(request, 'admin/access_denied.html')  
    

@user_passes_test(admin_required)
def admin_delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'کاربر با موفقیت حذف شد.')
    return redirect('admin_users_list')


@user_passes_test(admin_required)
def admin_delete_house(request, house_id):
    house = get_object_or_404(House, id=house_id)
    house.delete()
    messages.success(request, 'خانه با موفقیت حذف شد.')
    return redirect('admin_houses_list')


@user_passes_test(admin_required)
def admin_delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    messages.success(request, 'سفارش با موفقیت حذف شد.')
    return redirect('admin_orders_list')


@user_passes_test(admin_required)
def toggle_user_status(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_active = not user.is_active
    user.save()
    messages.success(request, f'کاربر {"فعال" if user.is_active else "غیرفعال"} شد.')
    return redirect('admin_users_list')


@user_passes_test(admin_required)
def toggle_house_status(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    house.is_active = not house.is_active
    house.save()
    messages.success(request, f'خانه {"فعال" if house.is_active else "غیرفعال"} شد.')
    return redirect('admin_houses_list')
