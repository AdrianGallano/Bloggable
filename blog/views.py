from django.shortcuts import render
from .models import Blog

def index(request):
    blog = Blog.objects.all()[0] 
    template = 'blog/index.html'
    context = {'blog':blog}
    print('this', blog)
    return render(request, template, context)

