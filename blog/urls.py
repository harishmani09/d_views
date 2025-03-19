from django.urls import path,include
from django.contrib import admin

from .views import post_model_list_view

urlpatterns = [
    path('',post_model_list_view,name='list'),
]


