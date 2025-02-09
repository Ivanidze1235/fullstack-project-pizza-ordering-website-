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
        orders = Order.objects.filter(usr=request.user)[::-1]
    else:
        orders = None
    return render(request, "index.html", {'orders':orders})

def order(request, pizza_id):
    print(request.path)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.usr = request.user
            order.pizza = Pizza.objects.get(id=pizza_id)
            order.save()
            return redirect('index')
        else:
            form = OrderForm()
            return render(request, "order.html")
    else:
        form = OrderForm()
        return render(request, "order.html", {'pizza':Pizza.objects.get(id=pizza_id), 'ordform':form})

def create(request):
    if request.method == "POST":
        form = PizzaCreationForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            return redirect("order", pizza.id)
        else:
            return render(request, 'create.html', {'form': form})
    else:
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
  