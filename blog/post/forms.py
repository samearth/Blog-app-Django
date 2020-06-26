from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['id','username', 'email' , 'password1' , 'password2']

class profileform(ModelForm):
    class Meta:
        model= profile
        fields = ['id','name','phone']

class post_form(forms.Form):
    title = forms.CharField(max_length=100)
    posts = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":90}))