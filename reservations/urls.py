from django.urls import path
from . import views

urlpatterns = [
    # path('signup/', views.signup_view, name='signup'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('hotels/', views.hotel_list_view, name='hotel_list'),
    # path('hotels/<int:hotel_id>/rooms/', views.room_list_view, name='room_list'),
    # path('rooms/<int:room_id>/reserve/', views.reserve_room_view, name='reserve_room'),
    path('', views.index_view, name='index'),
    path('hotels/', views.hotels_view, name='hotels'),
]
