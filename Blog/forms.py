from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class PenggunaForm(forms.ModelForm):
    class Meta :
        model = Pengguna
        fields =['namalengkap']
        labels = {'namalengkap':"Nama Lengkap"}
        widgets ={
            'namalengkap': forms.TextInput(attrs={'class':'form-control','placeholder': "Enter your full name here"})
            }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['judulBlog','isiBlog']
        judulBlog = forms.CharField(label='Judul Blog')
        isiBlog = forms.CharField(widget=forms.Textarea, label='Isi Blog')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username",
    widget=forms.TextInput(
        attrs={
        'class' : 'form-control',
        'placeholder' : 'Username',
        'type' : 'text',
        'name': 'username',
    }))

    password = forms.CharField(label="Password", 
    widget=forms.PasswordInput(
        attrs={
        'class' : 'form-control',
        'placeholder' : 'Password',
        'type' : 'password',
        'name': 'password',
    }))

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type' : 'password',
                'placeholder': 'Enter your password',
                'name': 'password',
            }
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type' : 'password',
                'placeholder': 'Confirm your password',
                'name': 'password',
            }
        )
    )
    class Meta :
        model = User
        fields= ("email",'username')
        labels = {'username':'Username','email':'Email',}
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder': "Enter your username here",  "autocomplete":"off"}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder': "Enter your email here",  "autocomplete":"off"}),
        }
        help_texts = {
            "username":None,
        }