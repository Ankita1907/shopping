from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'Shophome'),
    path('about/', views.about, name = 'Aboutus'),
    path('contact/', views.contact, name = 'ContactUs'),
    path('tracker', views.tracker, name = 'TrackingStatus'),
    path('search/', views.search, name = 'Search'),
    path('productview/', views.productview, name = 'productview'),
    path('checkout/', views.checkout, name = 'Checkout'),

]
