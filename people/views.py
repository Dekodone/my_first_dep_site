from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import person
from django.contrib import messages

# Create your views here.
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

#get all person
def getAll(request):
    mypeople = person.objects.all().values()
    template = loader.get_template('people.html')
    context = {
        'mypeople' : mypeople
    }
    return HttpResponse(template.render(context, request))

#get person info by id
def getById(request, id):
    myperson = person.objects.get(id=id)
    template = loader.get_template('person.html')
    context = {
        'myperson' : myperson
    }
    return HttpResponse(template.render(context, request))

#add methode
def add(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        emale = request.POST['emale']
        phone = request.POST['phone']
        age = request.POST['age']
        person.objects.create(firstname=firstname, lastname=lastname, emale=emale, phone=phone, age=age)
        messages.success(request,'Person has been added')

    return render(request,'add.html')
    # context = {
        
    # }
    # template = loader.get_template('add.html')
    # return HttpResponse(template.render(context, request))

#update methode
def update(request, id):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        emale = request.POST['emale']
        phone = request.POST['phone']
        age = request.POST['age']
        person.objects.filter(id=id).update(firstname=firstname, lastname=lastname, emale=emale, phone=phone, age=age)
        messages.success(request,'Person has been updated')
    myperson = person.objects.get(id=id)
    return render(request,'update.html',{'myperson':myperson})

#delete methode
def delete(request,id):
    person.objects.filter(id=id).delete()
    return render(request,'delete.html')

#test methodes
def say_hello(request):
    return HttpResponse("Hi Ayoub")

#test call template
def call_template(request):
    template = loader.get_template('first_page.html')
    return HttpResponse(template.render())