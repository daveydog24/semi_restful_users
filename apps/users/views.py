from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Users
# Create your views here.

def index(request):
    return render(request, 'users_templates/index.html', {"users": Users.objects.all()})

def new(request):
    return render(request, 'users_templates/new.html')

def edit(request, id):
    context = {
        'users': Users.objects.get(id=id)
    }
    return render(request, 'users_templates/edit.html', context)

def show(request, id):
    context = {
        'users': Users.objects.get(id=id)
    }
    return render(request, 'users_templates/show.html', context)

def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    # errors = Users.objects.validate_user(request.POST)
    
    # if len(errors):
    #     for tag, error in errors.iteritems():
    #         messages.error(request, error)
    #         return redirect('/users/new')
    # else:
    Users.objects.create(first_name=first_name, last_name=last_name, email=email)
    return redirect('/users')

def destroy(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    return redirect('/users')

def update(request):
    user = Users.objects.get(id=request.POST['id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect("/users/{}".format(user.id))