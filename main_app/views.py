from django.shortcuts import render
from .models import Cat

def index(request):
    cats = Cat.objects.all()
    return render(request, 'index.html', { 'cats':cats })

def show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'show.html', {'cat': cat})
