from django.urls import path, include
from . import views
from django.conf.urls import url
from .views import *
from django.contrib.auth.views import LoginView

app_name = "admins"

urlpatterns = [


    path('index', index, name='index'),

    path('', LoginView.as_view(redirect_authenticated_user=True), name="login"),

    #signup_manager
    path('signup_manager', signup_manager, name='signup_manager'),
    #signup_worker
    path('signup_worker', signup_worker, name='signup_worker'),
    #dashboard
    path('dashboard', dashboard, name='dashboard'),



    #Create Manager
    path('create_manager', create_manager, name='create_manager'),
    # Edit Manager
    url(r'^edit_manager/(?P<id>\d+)/$', edit_manager, name='edit_manager'),
    # Delete Manager
    url(r'^delete_manager/(?P<id>\d+)/$', delete_manager, name='delete_manager'),


    #Create Worker
    path('create_worker', create_worker, name='create_worker'),
    # Edit Worker
    url(r'^edit_worker/(?P<id>\d+)/$', edit_worker, name='edit_worker'),
    # Delete Worker
    url(r'^delete_worker/(?P<id>\d+)/$', delete_worker, name='delete_worker'),



    #Create Departament
    path('create_departament', create_departament, name='create_departament'),
    # Edit Manager
    url(r'^edit_departament/(?P<id>\d+)/$', edit_departament, name='edit_departament'),
    # Delete Departament
    url(r'^delete_departament/(?P<id>\d+)/$', delete_departament, name='delete_departament'),

    

    #List Manager
    path('list_manager', list_manager, name='list_manager'),
    #List Worker
    path('list_worker', list_worker, name='list_worker'),
    #List Departament
    path('list_departament', list_departament, name='list_departament'),


]