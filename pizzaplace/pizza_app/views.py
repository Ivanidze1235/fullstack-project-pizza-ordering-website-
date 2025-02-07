from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import *

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(usr=request.user)
    else:
        orders = None
    return render(request, "index.html", {'orders':orders})

def order(request, pizza=None):
    return render(request, "order.html", {'pizza':pizza})

def create(request):
    if request.method == "POST":
				# create a new copy of the form with the data the user 
				# entered , it is stored in request.POST

        form = PizzaCreationForm(request.POST)
        
        if form.is_valid():
            pizza = form.save()
            order = Order(usr=request.user, pizza=pizza)
            order.save()
            
            return render(request, 'order.html', {'pizza':pizza})
        else:
						# form has errors
						# send the form back to the user
            return render(request, 'create.html', {'form': form})
    else:
        # normal get reuqest, user wants to see the form 
        form = PizzaCreationForm()
        return render(request, 'create.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form, 'title':'register here'})
  