

from django.urls import path
from .views import home_fun

urlpatterns = [
    path('', home_fun, name='home' ),
]
