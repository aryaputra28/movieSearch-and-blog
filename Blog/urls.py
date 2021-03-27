from django.urls import path

from . import views

app_name = 'Blog'

urlpatterns = [
    path('blog', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/',views.signUp, name = 'signup'),
    path('logout/', views.logout_view, name ='logout'),
    path('createblog/', views.blogCreator, name = 'blogCreator'),
    path('listBlog/', views.allBlogs, name= 'allBlogs'),
    path('<int:id>',views.blogDetail),
    path('deleteBlog/<str:id>', views.deleteBlog,name="Blog_delete"),
    path('UpdateBlog/<str:id>',views.updateBlog,name="Blog_update")
]