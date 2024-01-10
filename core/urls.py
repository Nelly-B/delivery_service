from .import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('customer/', views.customer_page, name='customer_page'),
    path('courier/', views.courier_page, name='courier_page')
]