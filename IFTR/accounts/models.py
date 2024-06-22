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

class FarmerQuery(models.Model):
    fq_id= models.ForeignKey(Farmer, on_delete=models.CASCADE,related_name="farmer_query")
    fq_area_ploughed = models.CharField(max_length=100)
    fq_season = models.CharField(max_length=100)
    fq_crop_grown = models.CharField(max_length=100)
    fq_seeds_used = models.CharField(max_length=1000)
    fq_date_of_seed_sown = models.DateField()
    fq_transplanting = models.CharField(max_length=100)
    fq_irrigation = models.CharField(max_length=100)
    fq_fertilizers_used = models.CharField(max_length=1000)
    fq_date_of_harvest=models.DateField()
    fq_yield = models.IntegerField(max_length=1000)

    def __str__(self):
        return f'{self.fq_id.f_name}'

class Volunteer(models.Model):
    v_id= models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    v_name=  models.CharField(max_length=100)
    v_aadhar_number= models.BigIntegerField()
    v_contact_number= models.BigIntegerField()
    v_location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.v_name}'








