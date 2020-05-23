from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from django.shortcuts import redirect
from .forms import *

# Create your views here.\
@csrf_exempt
def index(request):
    get_todo=Todo.objects.all().order_by("-added_date")
    form=TaskForm()
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo/')



    return render(request,'blog_index.html',{'todos':get_todo,'form':form})

@csrf_exempt
def add_todo(request):
    current_date=timezone.now()
    content=request.POST["content"]
    Todo.objects.create(added_date=current_date,text=content)
    return redirect("/todo/")
@csrf_exempt
def delete_todo(request,todo_id):
    item=Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        item.delete()
    return redirect("/todo/")

@csrf_exempt
def update_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TaskForm(instance=todo)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/todo/')

    else:

        form = TaskForm(instance=todo)


    context = {'form': form}

    context={'forms':form}
    return render(request,'blog_update.html', context)





