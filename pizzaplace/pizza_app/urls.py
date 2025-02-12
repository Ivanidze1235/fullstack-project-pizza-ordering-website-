from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('order/<int:pizza_id>', views.order, name="order"),
   path('confirmation/<int:order_id>', views.confirmation, name="confirmation"),
   path('create/', views.create, name="create"),
   path('accounts/signup/', views.signup, name="signup"),
]