from django.urls import path
from .views import *

urlpatterns = [
    path('', convert_img, name='convert_img'),
]