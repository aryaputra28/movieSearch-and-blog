from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('bookmarks', views.bookmarks, name="bookmarks"),
    path('likes',views.likes, name = "likes")
]