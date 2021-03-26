from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def bookmarks(request):
    return render(request, 'home/bookmark.html')

def likes(request):
    return render(request, 'home/likes.html')