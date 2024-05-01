from django.urls import path
from .views import catagories,laptop,phone
urlpatterns = [
    path('', catagories, name='catagories'),
    path('laptop/', laptop, name='laptop'),
    path('phone/', phone, name='phone'),
]
