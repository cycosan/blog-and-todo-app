from django.forms import forms
from django.forms import ModelForm
from .models import *
class TaskForm(ModelForm):
    class Meta():
        model = Todo
        fields = '__all__'

