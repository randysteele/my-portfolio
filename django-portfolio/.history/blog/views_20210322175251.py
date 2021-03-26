from django.shortcuts import render

# Create your views here.

def allblogs(request):
    return render(request, 'allblogs.html')
