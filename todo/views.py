from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from django.shortcuts import redirect


# Create your views here.\
@csrf_exempt
def index(request):
    get_todo=Todo.objects.all().order_by("-added_date")
    return render(request,'blog_index.html',{'todos':get_todo})
@csrf_exempt
def add_todo(request):
    current_date=timezone.now()
    content=request.POST["content"]
    Todo.objects.create(added_date=current_date,text=content)
    return redirect("/todo/")
@csrf_exempt
def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect("/todo/")





