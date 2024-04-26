from django.urls import path
from .views import python_app

urlpatterns = [
    path('', python_app, name='python_app' ),
]
