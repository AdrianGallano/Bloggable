from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
import os
from django.conf import settings
def index(request):
    blog = Blog.objects.order_by('date_published')[0] 
    template = 'blog/index.html'
    context = {'blog':blog,}
    return render(request, template, context)

def blogs(request, pk):
    return HttpResponse('Blog' + str(pk))