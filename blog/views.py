from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    context = {}
    
    return render(request, template, context)

