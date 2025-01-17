from django.urls import path
from . import views

urlpatterns = [
    # Admin Panel
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    
    # Host-related Management
    path('admin_panel/host_requests/', views.host_requests, name='host_requests'),
    path('host-houses/', views.host_houses, name='host_houses'),
    # Action URLs (Moved to Admin Panel view)
    path('admin_panel/toggle_user_status/<int:user_id>/', views.toggle_user_status, name='toggle_user_status'),
    path('admin_panel/delete_user/<int:user_id>/', views.admin_delete_user, name='admin_delete_user'),
    path('admin_panel/toggle_house_status/<int:house_id>/', views.toggle_house_status, name='toggle_house_status'),
    path('admin_panel/delete_house/<int:house_id>/', views.admin_delete_house, name='admin_delete_house'),
    path('admin_panel/delete_order/<int:order_id>/', views.admin_delete_order, name='admin_delete_order'),
]
