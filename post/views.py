from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
from .models import Posts

# Create your views here.
def custom_404(request, exception):

    # Redirect to the specified URL
    return redirect(index)
def index(request):
    posts = Posts.objects.all()
    return render(request,'index.html',{'posts':posts})

def posts(request,pk):
    post = Posts.objects.get(id=pk)
    return render(request,'posts.html',{'post':post})

def write(request):
    return render(request,'write.html')

def post(request):
    if request.method=='POST':
        title = str(request.POST['title'])
        body = str(request.POST['body'])
        
        if title.strip() and body.strip():
            user = Posts.objects.create(title= title,body = body)
            user.save()
    # return render(request,'download.html',{'amount':word})
    return redirect('write')