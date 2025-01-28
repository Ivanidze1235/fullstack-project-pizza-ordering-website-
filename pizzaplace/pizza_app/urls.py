from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"), #names of pages
   path('order/', views.order, name="order"),
   
]