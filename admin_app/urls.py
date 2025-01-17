from django.urls import path
from . import views

urlpatterns = [
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('management/users/', views.admin_users_list, name='admin_users_list'),
    path('management/houses/', views.admin_houses_list, name='admin_houses_list'),
    path('management/orders/', views.admin_orders_list, name='admin_orders_list'),
    path('management/add_admin/', views.admin_add_admin, name='admin_add_admin'),
    path('management/users/delete/<int:user_id>/', views.admin_delete_user, name='admin_delete_user'),
    path('management/houses/delete/<int:house_id>/', views.admin_delete_house, name='admin_delete_house'),
    path('management/orders/delete/<int:order_id>/', views.admin_delete_order, name='admin_delete_order'),
    path('management/users/toggle/<int:user_id>/', views.toggle_user_status, name='toggle_user_status'),
    path('management/houses/toggle/<int:house_id>/', views.toggle_house_status, name='toggle_house_status'),
    path('host-houses/', views.host_houses, name='host_houses'),
    path('management/host_requests/', views.host_requests, name='host_requests'),
] 

