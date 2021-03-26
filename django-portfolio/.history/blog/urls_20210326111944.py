from django.urls import path
from  . import views 
from .views import get_blogs, blogBody

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/',views.detail, name='detail' ),
    path("blog", blog, name="blog"),
] 
