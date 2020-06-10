from django.db import models
from manager.models import Managers, Departament, User
from manager.validators import validate_file_size
from phone_field import PhoneField

class Worker(models.Model):
    manager = models.ForeignKey(Managers, on_delete=models.CASCADE)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_active = models.BooleanField(default = False)
    profile_picture = models.ImageField(upload_to='avatar/worker/%Y/%m/%d', default='avatar/default.jpg',
                                 verbose_name='avatar', null=True, blank=True, validators=[validate_file_size])
    ## 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = PhoneField(blank=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Task(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    asign = models.ForeignKey(Managers, on_delete=models.CASCADE)
    #task description
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    #dates
    start_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    end_date = models.DateField(blank=True, null=True)
    #status
    is_finish = models.BooleanField(default = False)

    def task_complete(self):

        task = Task.objects.filter(worker=self.worker, is_finish=True).count()
        return str(task)
    
    def task_pending(self):

        task = Task.objects.filter(worker=self.worker, is_finish=False).count()
        return str(task)

class Report(models.Model):
    date = models.DateField(auto_now_add=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200, blank=True, null=True)