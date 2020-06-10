from .models import Worker, Task, Report
from django import forms
from manager.models import Managers


class WorkerRegistroForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = '__all__'
        exclude = ['user', 'is_active']

class WorkerUpdateForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = '__all__'
        exclude = ['user', 'is_active', 'departament', 'manager']

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['asign']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(TaskForm, self).__init__(*args, **kwargs)
        manager = Managers.objects.get(user=user)
        self.fields['worker'].queryset = Worker.objects.filter(manager=manager)    

class OtherTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['is_finish']
        exclude = ['asign']

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = '__all__'
        exclude = ['worker', 'observation']


class ReportUpdateForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = '__all__'
        exclude = ['worker']

        