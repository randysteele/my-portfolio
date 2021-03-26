from django.contrib import admin

# Register your models here.

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Blog)
