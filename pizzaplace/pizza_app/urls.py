from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"), #names of pages
   path('order/<int:pizza_id>', views.order, name="order"),
   path('create/', views.create, name="create"),
   path('accounts/signup/', views.signup, name="signup"),
]