from django.urls import path
from . import views

urlpatterns=[
    path('lv/', views.LaptopView, name='laptopform_url'),
    path('sl/', views.showLaptop, name='showlaptop_url'),
    path('ul/<int:id>/', views.updateLaptop, name='update_url'),
    path('dl/<int:id>/', views.deleteLaptop, name='delete_url')
    ]

