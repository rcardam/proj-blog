from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.

def home(request):
    vposts = Post.objects.all()
    context = {
        'posts': vposts
    }
    return render(request,"blog/home.html", context)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request,'blog/post_detail.html', context)