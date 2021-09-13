from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

def index(request):
    nav = True
    blog = Blog.objects.order_by('-date_published')[0]
    template = 'blog/index.html'
    context = {'blog':blog, 'nav':nav}
    print(blogs)
    return render(request, template, context)

def blogs(request):
    blogs = Blog.objects.order_by('-date_published')
    template = 'blog/blogs.html'
    context = {'blogs':blogs}
    return render(request, template, context)

def blog(request, pk):
    template = 'blog/blog.html'
    context ={}
    return render(request, template, context)


def send_email(request):
    return HttpResponse('SENT')