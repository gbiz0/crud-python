from django.shortcuts import render
from .models import Person

def home(request):
    people = Person.objects.all()
    return render(request, 'index.html', {"people": people})

def save(request):
    request.method == 'POST'
    vname = request.POST.get('name')
    vage = request.POST.get('age')
    Person.objects.create(name=vname, age=vage)
    people = Person.objects.all()
    return render(request, 'index.html', {"people": people})