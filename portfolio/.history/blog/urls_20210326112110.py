from django.urls import path
from  . import views 
from .views import get_blogs, blogBody
from blog.views import allblogs

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('blog/<int:blog_id>/',views.detail, name='blog' ),
    path("blog", allblogs, name="blog"),
] 
