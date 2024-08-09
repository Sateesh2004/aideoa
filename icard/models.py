# models.py
from django.db import models
from django.contrib.auth.models import User
class Person(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,blank=True,)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    current_company = models.CharField(max_length=15,default='none')
    photo = models.ImageField(upload_to='photos/')

    
