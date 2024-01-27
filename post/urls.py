from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('posts/<str:pk>',views.posts,name='posts'),
    path('write/submit/URL/blogPostWrite',views.write,name='write'),
    path('write/submit/URL/post',views.post,name='post'),
    
]

