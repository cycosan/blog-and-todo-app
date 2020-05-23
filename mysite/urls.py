"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static
from todo import views as todo_views

urlpatterns = [
    path('name/post/<slug:slug>',blog_views.post, name='detail'),
    #path('polls/',include('blog.urls')),
    path('',blog_views.IndexList.as_view()),
    path('about/',blog_views.about),
    path('admin/', admin.site.urls),
    path('todo/',todo_views.index),
    path('todo/add_todo/',todo_views.add_todo),
    path('todo/delete_todo/<int:todo_id>/', todo_views.delete_todo),
    path('todo/update_todo/<str:todo_id>',todo_views.update_todo,name="todo_update"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

