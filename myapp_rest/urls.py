from django.urls import path

from .views import *

urlpatterns = [
    path('images/', ImageListView.as_view()),
    path('image-detail/<int:pk>', ImageDetailView.as_view()),
    path('image-change/<int:pk>/', ImageChangeView.as_view()),
    path('image-create', ImageCreateView.as_view()),
]