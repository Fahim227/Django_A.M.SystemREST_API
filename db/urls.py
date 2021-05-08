from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home,name='home'),
    # path('delete/<int:id>', views.delete,name='delete'),
    path('getAllAvailableFlats/', views.show_flatsInJson,name='getAvailableFlats'),
    path('insertApartment/', views.insert_Apartment_info,name='insert_Apartment_info'),
    path('insertReport/', views.insert_Report,name='insert_Report'),
    path('insertBill/', views.insert_bill,name='insert_bill'),
    path('trial/', views.trial,name='trial'),
    path('getOwnerFlats/', views.getOwnedFlats,name='ownedFlats'),
    path('getAllFlats/',views.show_flats,name='AllFlats')
]
