from django.urls import path
from  . import views 
from blog.views import allblogs

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('blog/<int:id>/',views.detail, name='blog' ),
    path("blog", allblogs, name="blog"),
] 
