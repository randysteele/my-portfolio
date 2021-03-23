from django.urls import path
import views 

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
] 
