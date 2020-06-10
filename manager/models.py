from django.db import models
from .validators import validate_file_size
from phone_field import PhoneField
from admins.models import User


class Managers(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    profile_picture = models.ImageField(upload_to='avatar/manager/%Y/%m/%d', default='avatar/default.jpg',
                                 verbose_name='avatar', null=True, blank=True, validators=[validate_file_size])
    ## 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = PhoneField(blank=True)
    # 
    is_active = models.BooleanField(default = False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Departament(models.Model):

    name = models.CharField(max_length=50)
    responsible = models.OneToOneField(Managers, on_delete=models.CASCADE, primary_key=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

