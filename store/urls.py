from django.urls import path
from . import views
from phone import views as phoneViews
from computer import views as pcViews

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('register/',views.register_user, name='register'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('cart/', views.view_cart, name='viewCart'),
    path('cart/add', views.add_to_cart, name='cartAdd'),
    path('phones/', phoneViews.show_phones, name='showPhones'),
    path('phone-details/<int:id>', phoneViews.phone_details, name='phoneDetails'),
    path('computers/', pcViews.show_pcs, name='showComputers'),
    path('computer-details/<int:id>', pcViews.pc_details, name='pcDetails'),
    path('checkout/phone/<int:id>/', phoneViews.phone_checkout,name='phoneCheckout'),
    path('checkout/computer/<int:id>/', pcViews.pc_checkout,name='pcCheckout'),

]