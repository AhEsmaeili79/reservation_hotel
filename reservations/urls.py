from django.urls import path
from . import views

urlpatterns = [
    path('user/orders/', views.user_orders, name='user_orders'),
    path('cancel_order/<int:pk>/', views.cancel_order, name='cancel_order'),
    path('host_reservations/', views.host_reservations, name='host_reservations'),
    path('houses/<int:pk>/order/', views.order_house, name='order_house'),
]

