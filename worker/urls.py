from . import views
from django.conf.urls import url
from .views import *
from django.urls import path, include

app_name = "worker"

urlpatterns = [


    #Look Tasks
    path('my_tasks', my_tasks, name='my_tasks'),
    # Finish Task
    url(r'^finish_task/(?P<id>\d+)/$', finish_task, name='finish_task'),

    # Create Report
    path('create_report', create_report, name='create_report'),
    # My report
    path('my_report', my_report, name='my_report'),

    # My profile
    path('profile_worker', profile_worker, name='profile_worker'),
   


]