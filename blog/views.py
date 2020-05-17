from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView

# Create your views here.
def index(request):
    posts=Post.objects.all()
    print(posts)
    return render(request,'index.html',{'posts':posts})
def post(request,slug):
    posts=Post.objects.all()
    return render(request, 'post.html',{'post':get_object_or_404(Post,slug=slug),'posts':posts})
def about(request):
    return render(request,'about.html',{})
class IndexList(ListView):
    queryset = Post.objects.all()
    template_name = 'index.html'