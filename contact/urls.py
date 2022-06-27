from django.urls import path
from .views import ContactRUD, contact_list
from rest_framework.decorators import api_view 

urlpatterns = [
    path('contacts/',contact_list,name='contact_list'),
    path('contacts/<int:pk>/',ContactRUD.as_view(),name='contact_detail'),
]