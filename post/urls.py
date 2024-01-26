from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('posts/<str:pk>',views.posts,name='posts'),
    
]
