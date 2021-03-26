from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),
] 
