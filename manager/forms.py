from .models import Managers, Departament
from django import forms

class ManagersRegistroForm(forms.ModelForm):

    class Meta:
        model = Managers
        fields = '__all__'
        exclude = ['user', 'is_active']

class DepartamentForm(forms.ModelForm):

    class Meta:
        model = Departament
        fields = '__all__'
        