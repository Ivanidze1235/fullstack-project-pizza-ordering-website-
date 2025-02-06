
from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
class UserRegisterForm(UserCreationForm):
    phone_no = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'phone_no', 'password1', 'password2']

class PizzaCreationForm(forms.ModelForm):

    size = forms.ChoiceField(choices=[(si.size, si.size) for si in models.Sizes.objects.all()], widget=forms.Select)
    sauce = forms.ChoiceField(choices=[(sau.sauce, sau.sauce) for sau in models.Sauces.objects.all()], widget=forms.Select)
    cheese = forms.ChoiceField(choices=[(che.cheese, che.cheese) for che in models.Cheeses.objects.all()], widget=forms.Select)    

    class Meta:
        model = models.Pizza

        fields = ['size', 'crust', 'sauce', 'cheese', 'pepperoni', 'chicken', 'ham', 'pineapple', 'peppers', 'mushrooms', 'onions']