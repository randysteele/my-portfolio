from django.shortcuts import render, get_object_or_404
import requests
from .models import Blog

# Create your views here.

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})


def detail(request, blog_id):
  detailblog =  get_object_or_404(Blog, pk=blog_id)
  return render(request, 'blog/detail.html', {'blog':detailblog})


def get_blogs(request):
   all_blogs = {}

   API_KEY = 'UU5XhQB4ciYQAv9joWrxhiVb'

   url = 'https://dev.to/api/articles/me/published'

   headers = {'api-key': API_KEY}

   response = requests.get(url, headers=headers)

   data = response.json()

   for i, item in enumerate (data):
      blog_data = Blog(
         title = data[i]['title'],
         description = data[i]['description'],
         cover_image = data[i]['cover_image'],
         blog_body = data[i]['body_markdown'],
         published_at = data[i]['published_at']
      )

      blog_data.save()

      all_blogs = Blog.objects.all().order_by('-published_at').distinct('published_at')

      return render (request, "blog.html", {"all_blogs": all_blogs})


def blogBody(request, id):
   blog = Blog.objects.get(id = id)

   return render (request, "allblogs.html", {"blog": blog})