from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import requests
import json
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers

# Create your views here.
def index(request):
    ownBlogs = Blog.objects.all()
    user = request.user
    context = {
        "ownBlog" : ownBlogs,
        "user" : user
    }
    return render(request, 'Blog/blog.html',context)

def allBlogs(request):
    all = Blog.objects.all()
    context ={
        'all':all,
    }
    return render(request, 'Blog/listBlogs.html',context)


def blogCreator(request):
    blog_form = BlogForm()
    blog_model = Blog.objects.all()
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            blog_form.save()
            blog_model.create(
                judulBlog = blog_form.cleaned_data.get('judulBlog'),
                isiBlog = blog_form.cleaned_data.get('isiBlog'),
                akun = request.user
            )
            print(request.user)
            return redirect('/blog')
    context = {
        'blog_form':blog_form,
        'blog_model':blog_model
    }
    return render(request, 'Blog/blogForum.html',context)




def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form2 = PenggunaForm(request.POST)
        userModel = Pengguna.objects.all()

        if form.is_valid() and form2.is_valid():
            user = form.save()
            userModel.create(
                namalengkap = form2.cleaned_data.get('namalengkap'),
                akun = user
            )
            login(request, user)
            return HttpResponseRedirect('/')

        else:
            for msg in form.error_messages:
                messages.error(request, 'Invalid entry')

    else:
        form = SignUpForm()
        form2 = PenggunaForm()

    context = {
        'form' : form,
        'form2': form2,
    }

    return render(request, "Blog/signup.html", context)

def login_view(request):
    if request.method == 'POST':
        valuenext = request.POST.get('next')
        form = LoginForm(data = request.POST)

        if form.is_valid():
            usernameInput = request.POST["username"]
            passwordInput = request.POST["password"]

            user = authenticate(request, username=usernameInput, password=passwordInput)

            if user is not None and valuenext == "":
                login(request, user)
                return redirect('home:index')
            if user is not None and valuenext != "":
                login(request, user)
                return redirect(valuenext)
        else:
            messages.error(request, 'Invalid entry')

    else:
        form = LoginForm()

    context = {
        'form' : form,
    }

    return render(request, 'Blog/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    form = LoginForm()
    response = {
        'form' : form,
    }
    return redirect('Blog:login')

def blogDetail(request,id):
    blogDetail = Blog.objects.get(id=id)
    context = {
        'blog':blogDetail
    }
    return render(request,'Blog/blogDetail.html',context)

def deleteBlog(request,id):
    item = Blog.objects.get(id=id)
    if request.method == 'POST' :
        item.delete()
        return redirect('/blog')

    return render(request, 'Blog/blogDelete.html',{'item':item})

def updateBlog(request,id):
    blogPilihan = Blog.objects.get(id=id)
    form = BlogForm(instance=blogPilihan)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blogPilihan)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    context = {
        'blog_form' :form
    }
    return render (request,'Blog/blogForum.html' ,context)