from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'login/index.html')

def create_user(request):

    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        this_user = User.objects.create(
                                        first_name=request.POST['first_name'],
                                        last_name=request.POST['last_name'],
                                        email=request.POST['email'],
                                        password= request.POST['password'],
                                        )
        request.session['first_name'] = this_user.first_name
        request.session['last_name'] = this_user.last_name
        request.session['email'] = this_user.email
        request.session['id'] = this_user.id
        messages.success(request, 'User Successfully Created')
        return redirect('/dashboard/',)

def login_check(request):
    all_users = User.objects.all()
    is_user = False
    for user in all_users:
        if user.email == request.POST['email']:
            is_user = True
    if is_user == False:
        messages.error(request, 'User does not exist', request)
        return redirect('/index')
    this_user = User.objects.get(email = request.POST['email'])
    if request.POST['password'] != this_user.password:
        messages.error(request, 'incorrect password')
        return redirect('/index', request)
    request.session['first_name'] = this_user.first_name
    request.session['last_name'] = this_user.last_name
    request.session['email'] = this_user.email
    request.session['id'] = this_user.id
    return redirect('/dashboard/',)

def myaccount(request, num):
    context = {
    'this_user' : User.objects.get(id=num)
    }
    return render(request, 'myaccount.html', context)

def update_myaccount(request, num):
    errors = User.objects.validator(request.POST)
    this_user = User.objects.get(id=num)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/myaccount/{num}', request)

    else:
        print(request.POST['first_name'])
        this_user.first_name=request.POST['first_name']
        this_user.last_name=request.POST['last_name']
        this_user.email=request.POST['email']
        this_user.password= request.POST['password']
        this_user.save()
        request.session['first_name'] = this_user.first_name
        request.session['last_name'] = this_user.last_name
        request.session['email'] = this_user.email
        messages.success(request, 'User Successfully Updated')
        return redirect('/quotes/', request,)

def logout(request,):
    request.session.clear()
    return redirect('/')