from django.urls import path
from .views import css_app

urlpatterns = [
    path('', css_app, name='css_app' ),
]
