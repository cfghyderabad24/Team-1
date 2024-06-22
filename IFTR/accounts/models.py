from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Farmer(models.Model):
    f_id = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    f_name= models.CharField(max_length=255)
    f_pincode= models.IntegerField()
    f_contact_number= models.BigIntegerField()
    

    def __str__(self):
        return f'{self.f_name}'









