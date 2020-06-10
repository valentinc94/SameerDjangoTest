from django.shortcuts import render, redirect
from admins.models import User
from django.contrib import messages
from manager.models import Managers, Departament
from django.http import HttpResponseRedirect
from worker.models import *
from worker.forms import *
import datetime
from datetime import datetime, time, date, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_worker, login_url='admins:dashboard')
#task by worker
def my_tasks(request):

    worker = Worker.objects.get(user=request.user)
    task = Task.objects.filter(worker=worker)

    if task:

        porcen_complete = Task.objects.filter(worker=worker, is_finish=True)
        num_complete = porcen_complete.count() * 100 / task.count() 

        porcent_incomplete = Task.objects.filter(worker=worker, is_finish=False)
        num_incomplete = porcent_incomplete.count() * 100 / task.count()

        diference = (porcen_complete.count() -  porcent_incomplete.count()) * 100 / task.count() 

        diference_two = (porcent_incomplete.count() - porcen_complete.count()) * 100 / task.count()
    
    else:
        num_complete = 0
        num_incomplete = 0
        diference = 0
        diference_two = 0


    return render(request, 'worker/task.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_worker, login_url='admins:dashboard')
#finish task by worker
def finish_task(request, id):
    task = Task.objects.get(id=id)
    today = date.today()

    if request.method == 'POST':
        form = OtherTaskForm(request.POST, instance=task)
        if form.is_valid():
            user = form.save(commit=False)
            user.end_date = today
            user.save()  
            messages.success(request, 'Task has been update successfully')
            return redirect('worker:my_tasks')
    else:
        form = OtherTaskForm(instance=task)
 
    return render(request, 'worker/modal.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_worker, login_url='admins:dashboard')
#create report / worker
def create_report(request):

    worker = Worker.objects.get(user=request.user)

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.worker = worker
            user.save()  
            messages.success(request, 'Report has been created successfully')
            return redirect('worker:my_report')
    else:
        form = ReportForm()
 
    return render(request, 'worker/report/create_report.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_worker, login_url='admins:dashboard')
#list of report by worker
def my_report(request):

    worker = Worker.objects.get(user=request.user)

    report = Report.objects.filter(worker=worker)

    return render(request, 'worker/report/my_report.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_worker, login_url='admins:dashboard')
#edit profile worker
def profile_worker(request):

    worker = Worker.objects.get(user=request.user)

    if request.method == 'POST':
        form = WorkerUpdateForm(request.POST, instance=worker)
        if form.is_valid():
            user = form.save(commit=False)
            user.worker = worker
            user.save()  
            messages.success(request, 'Profile has been update successfully')
            return redirect('worker:my_report')
    else:
        form = WorkerUpdateForm(instance=worker)
 
    return render(request, 'worker/profile.html', locals())


    