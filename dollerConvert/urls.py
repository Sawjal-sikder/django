from django.urls import path
from .views import dollerConvert
urlpatterns = [
    path('', dollerConvert, name='dollerConvert'),
]
