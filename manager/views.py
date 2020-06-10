from django.shortcuts import render, redirect
from admins.models import User
from django.contrib import messages
from manager.models import Managers, Departament
from django.http import HttpResponseRedirect
from worker.models import *
from worker.forms import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_manager, login_url='admins:dashboard')
#List Task
def my_task(request):

    manager = Managers.objects.get(user=request.user)
    task = Task.objects.filter(asign=manager)

    return render(request, 'manager/task.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_manager, login_url='admins:dashboard')
#Create Task
def create_task(request):

    manager = Managers.objects.get(user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.asign = manager
            user.save()  
            messages.success(request, 'Task has been created successfully')
            return redirect('manager:my_task')
    else:
        form = TaskForm(user=request.user)
    
    return render(request, 'manager/create_task.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_manager, login_url='admins:dashboard')
#Edit Task
def edit_task(request, id):

    manager = Managers.objects.get(user=request.user)
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.asign = manager
            user.save()  
            messages.success(request, 'Task has been created successfully')
            return redirect('manager:my_task')
    else:
        form = TaskForm(instance=task, user=request.user)
    
    return render(request, 'manager/create_task.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_manager, login_url='admins:dashboard')
# Delete Task
def delete_task(request, id):

    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        raise Http404("Task Doesn't exist")
    task.delete()
    messages.success(request, 'Task Delete successfullt!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_manager, login_url='admins:dashboard')
#List my Works
def my_works(request):

    manager = Managers.objects.get(user=request.user)

    workers = Worker.objects.filter(manager=manager)

    return render(request, 'manager/workers.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_manager, login_url='admins:dashboard')
#Edit my profile
def my_works(request):

    manager = Managers.objects.get(user=request.user)

    workers = Worker.objects.filter(manager=manager)

    return render(request, 'manager/workers.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_manager, login_url='admins:dashboard')
#Reports
def reports(request):

    manager = Managers.objects.get(user=request.user)

    workers = Worker.objects.filter(manager=manager)

    report = Report.objects.filter(worker__in=workers)

    return render(request, 'manager/reports.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_manager, login_url='admins:dashboard')
#edit report
def edit_report(request, id):

    report = Report.objects.get(id=id)

    if request.method == 'POST':
        form = ReportUpdateForm(request.POST, instance=report)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()  
            messages.success(request, 'Report has been update successfully')
            return redirect('manager:reports')
    else:
        form = ReportUpdateForm(instance=report)
 
    return render(request, 'manager/report_edit.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_manager, login_url='admins:dashboard')
#edit profile
def edit_profile(request):

    profile = Managers.objects.get(user=request.user)

    if request.method == 'POST':
        form = ManagersRegistroForm(request.POST, instance=profile)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()  
            messages.success(request, 'Report has been update successfully')
            return redirect('manager:reports')
    else:
        form = ManagersRegistroForm(instance=profile)
 
    return render(request, 'manager/profile.html', locals())