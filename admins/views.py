from django.shortcuts import render, redirect
from .models import User
from .forms import UCFWithEmail
from django.contrib import messages
from manager.forms import ManagersRegistroForm, DepartamentForm
from manager.models import Managers, Departament
from django.http import HttpResponseRedirect
from worker.models import Worker
from worker.forms import WorkerRegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout

def index(request):

    return render(request, 'index.html')

def signup_manager(request):

    if request.method == 'POST':
        user_form = UCFWithEmail(request.POST, prefix="user")
        manager_form = ManagersRegistroForm(request.POST, prefix="manager")
        if user_form.is_valid() and manager_form.is_valid():
            user = user_form.save(commit=False)
            user.is_manager = True
            user.email = str(user.username)
            user.save()  # This will load the Profile created by the Signal
            manager = manager_form.save(commit=False)
            manager.user = user
            manager.save()
            login(request, user)
            messages.success(request, 'Manager has been created successfully, please confirm your email!')
            return redirect('admins:dashboard')
    else:
        user_form = UCFWithEmail(prefix="user")
        manager_form = ManagersRegistroForm(prefix="manager")
    
    return render(request, 'admins/signup/manager.html', locals())

def signup_worker(request):

    if request.method == 'POST':
        user_form = UCFWithEmail(request.POST, prefix="user")
        worker_form = WorkerRegistroForm(request.POST, prefix="worker")
        if user_form.is_valid() and worker_form.is_valid():
            user = user_form.save(commit=False)
            user.is_worker = True
            user.email = str(user.username)
            user.save()  # This will load the Profile created by the Signal
            worker = worker_form.save(commit=False)
            worker.user = user
            worker.save()
            login(request, user)
            messages.success(request, 'Worker has been created successfully, please confirm your email!')
            return redirect('admins:dashboard')
    else:
        user_form = UCFWithEmail(prefix="user")
        worker_form = WorkerRegistroForm(prefix="worker")
    
    return render(request, 'admins/signup/worker.html', locals())



@login_required(redirect_field_name='/')
def dashboard(request):

    manager_ = Managers.objects.all()

    return render(request, 'users/dashboard.html')


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_superuser, login_url='admins:dashboard')
#lista manager
def list_manager(request):
    manager = Managers.objects.all()

    return render(request, 'admins/manager/list_manager.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_superuser, login_url='admins:dashboard')
#Create Manager
def create_manager(request):

    if request.method == 'POST':
        user_form = UCFWithEmail(request.POST, prefix="user")
        manager_form = ManagersRegistroForm(request.POST, prefix="manager")
        if user_form.is_valid() and manager_form.is_valid():
            user = user_form.save(commit=False)
            user.is_manager = True
            user.email = str(user.username)
            user.save()  # This will load the Profile created by the Signal
            manager = manager_form.save(commit=False)
            manager.user = user
            manager.save()
            messages.success(request, 'Manager has been created successfully, please confirm your email!')
            return redirect('admins:list_manager')
    else:
        user_form = UCFWithEmail(prefix="user")
        manager_form = ManagersRegistroForm(prefix="manager")
    
    return render(request, 'admins/manager/create_manager.html', locals())

@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_superuser, login_url='admins:dashboard')
#Edit Manager
def edit_manager(request, id):


    manager_user = Managers.objects.get(user_id=id)

    if request.method == 'POST':
        manager_form = ManagersRegistroForm(request.POST, prefix="manager", instance=manager_user)
        if manager_form.is_valid():
            manager = manager_form.save(commit=False)
            manager.save()
            messages.success(request, 'Manager has been update successfully!')
            return redirect('admins:list_manager')
    else:
        manager_form = ManagersRegistroForm(prefix="manager", instance=manager_user)
    
    return render(request, 'admins/manager/create_manager.html', locals())



@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_superuser, login_url='admins:dashboard')
# Delete Manager
def delete_manager(request, id):

    try:
        manager = Managers.objects.get(user_id=id)
        user = User.objects.get(id=id)
    except Managers.DoesNotExist:
        raise Http404("Manager Doesn't exist")
    manager.delete()
    user.delete()
    messages.success(request, 'Manager Delete successfullt!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_superuser, login_url='admins:dashboard')
#List worker
def list_worker(request):
    worker = Worker.objects.all().order_by('user')

    return render(request, 'admins/worker/list_worker.html', locals())




@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_superuser, login_url='admins:dashboard')
#Create Worker
def create_worker(request):


    if request.method == 'POST':
        user_form = UCFWithEmail(request.POST, prefix="user")
        worker_form = WorkerRegistroForm(request.POST, prefix="worker")
        if user_form.is_valid() and worker_form.is_valid():
            user = user_form.save(commit=False)
            user.is_worker = True
            user.email = str(user.username)
            user.save()  # This will load the Profile created by the Signal
            worker = worker_form.save(commit=False)
            worker.user = user
            worker.save()
            messages.success(request, 'Worker has been created successfully, please confirm your email!')
            return redirect('admins:list_worker')
    else:
        user_form = UCFWithEmail(prefix="user")
        worker_form = WorkerRegistroForm(prefix="worker")
    
    return render(request, 'admins/worker/create_worker.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_superuser, login_url='admins:dashboard')
#Edit Worker
def edit_worker(request, id):


    worker_user = Worker.objects.get(user_id=id)

    if request.method == 'POST':
        worker_form = WorkerRegistroForm(request.POST, instance=worker_user)
        if worker_form.is_valid():
            worker = worker_form.save(commit=False)
            worker.save()
            messages.success(request, 'Worker has been update successfully!')
            return redirect('admins:list_worker')
    else:
        worker_form = WorkerRegistroForm(instance=worker_user)
    
    return render(request, 'admins/worker/create_worker.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_superuser, login_url='admins:dashboard')
#Delete Worker
def delete_worker(request, id):

    try:
        worker_user = Worker.objects.get(user_id=id)
        user = User.objects.get(id=id)
    except Worker.DoesNotExist:
        raise Http404("Worker Doesn't exist")
    worker_user.delete()
    user.delete()
    messages.success(request, 'Worker Delete successfullt!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_superuser, login_url='admins:dashboard')
#List Departament
def list_departament(request):
    departament = Departament.objects.all().order_by('create_date')

    return render(request, 'admins/departament/list_departament.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_superuser, login_url='admins:dashboard')
#Create Departament
def create_departament(request):

    if request.method == 'POST':
        form = DepartamentForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save() 
            messages.success(request, 'Departament has been created successfully')
            return redirect('admins:list_departament')
    else:
        form = DepartamentForm()
    
    return render(request, 'admins/departament/create_departament.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_superuser, login_url='admins:dashboard')
#Edit Departament
def edit_departament(request, id):

    departament = Departament.objects.get(responsible_id=id)

    if request.method == 'POST':
        form = DepartamentForm(request.POST, instance=departament)
        if form.is_valid():
            user = form.save(commit=False)
            user.save() 
            messages.success(request, 'Departament has been created successfully')
            return redirect('admins:list_departament')
    else:
        form = DepartamentForm(instance=departament)
    
    return render(request, 'admins/departament/create_departament.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_superuser, login_url='admins:dashboard')
#Delete Departament
def delete_departament(request, id):

    try:
        departament = Departament.objects.get(responsible_id=id)
    except Departament.DoesNotExist:
        raise Http404("Departament Doesn't exist")
    departament.delete()
    messages.success(request, 'Departament Delete successfullt!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))