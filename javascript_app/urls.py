from django.urls import path
from .views import javascript_app

urlpatterns = [
    path('', javascript_app, name='javascript_app'),
]
