from django.urls import path
from .views import html_app

urlpatterns = [
    path('', html_app, name='html_app' ),
]
