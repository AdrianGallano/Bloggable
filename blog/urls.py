from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<uuid:pk>', views.latest, name='latest'),
    path('send_email', views.send_email, name='send_email'),
]

