from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
import os
from django.conf import settings
def index(request):
    nav = True
    blog = Blog.objects.order_by('date_published')[0] 
    template = 'blog/index.html'
    context = {'blog':blog, 'nav':nav}
    return render(request, template, context)

def blogs(request):
    template = 'blog/blogs.html'
    context = {}
    return render(request, template, context)

def latest(request, pk):
    template = 'blog/latest.html'
    context ={}
    return render(request, template, context)


def send_email(request):
    return HttpResponse('SENT')