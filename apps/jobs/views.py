from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Job
from ..login.models import User

def dashboard(request):
    this_user = User.objects.get(id=request.session['id'])

    context = {
        'jobs' : Job.objects.all(), 'taken_jobs' : this_user.jobs.all(),
    }
    return render(request,'jobs/dashboard.html', context)

def new_job(request):

    return render(request,'jobs/new.html')

def create_job(request):
    errors = Job.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/jobs/new', request)

    else:
        category_str = ''
        if 'other' in request.POST:
            category_str += request.POST['other']
        if 'garden' in request.POST:
            category_str += request.POST['garden']
        if 'electrical' in request.POST:
            category_str += request.POST['electrical']
        if 'pet_care' in request.POST:
            category_str += request.POST['pet_care']

        this_job = Job.objects.create(
                                        job_poster=User.objects.get(id=request.session['id']),
                                        title=request.POST['title'],
                                        location=request.POST['location'],
                                        description=request.POST['description'],
                                        job_type=category_str,
                                        )
        messages.success(request, 'Job Successfully Created')
        return redirect('/dashboard', request,)


def read_job(request, num):
    context = {
        'this_job' : Job.objects.get(id=num)
    }
    return render(request,'jobs/read.html', context)

def edit_job(request, num):
    context = {
        'this_job' : Job.objects.get(id=num)
    }
    return render(request,'jobs/edit.html', context)

def update_job(request, num):
    errors = Job.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/jobs/edit/{num}/')
    else:
        this_job = Job.objects.get(id=num)
        category_str = ''
        if 'other' in request.POST:
            category_str += request.POST['other']
        if 'garden' in request.POST:
            category_str += request.POST['garden']
        if 'electrical' in request.POST:
            category_str += request.POST['electrical']
        if 'pet_care' in request.POST:
            category_str += request.POST['pet_care']

        this_job.title = request.POST['title']
        this_job.location = request.POST['location']
        this_job.description = request.POST['description']
        this_job.job_type = category_str
        this_job.save()
        return redirect(f'/jobs/{num}/')

def delete_job(request, num):
    to_delete = Job.objects.get(id=num)
    to_delete.delete()
    return redirect('/dashboard/', request)

# for users taking jobs

def add(request, num):
    this_job = Job.objects.get(id=num)
    this_user = User.objects.get(id=request.session['id'])
    # if not this_job.users.count() ==0:
    this_job.users.add(this_user)
    # else:
    #     this_job.users.remove(this_user)
    return redirect('/dashboard/', request)

def give_up (request, num):
    this_job = Job.objects.get(id=num)
    this_user = User.objects.get(id=request.session['id'])
    # if this_job.users.get(id=this_user.id):
    this_job.users.remove(this_user)
    return redirect('/dashboard/', request)

