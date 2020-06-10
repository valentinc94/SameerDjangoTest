from django.urls import path, include
from . import views
from django.conf.urls import url
from .views import *

app_name = "manager"

urlpatterns = [

    # My Tasks
    path('my_task/', my_task, name='my_task'),
     # My Workers
    path('my_works/', my_works, name='my_works'),
    # Create Task
    path('create_task/', create_task, name='create_task'),
    # Edit Manager
    url(r'^edit_task/(?P<id>\d+)/$', edit_task, name='edit_task'),
    # Delete Manager
    url(r'^delete_task/(?P<id>\d+)/$', delete_task, name='delete_task'),

    #reports
    path('reports/', reports, name='reports'),
    # Edit Manager
    url(r'^edit_report/(?P<id>\d+)/$', edit_report, name='edit_report'),

    #profile
    path('edit_profile/', edit_profile, name='edit_profile'),


]