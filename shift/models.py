# models.py
from django.db import models

class JobShift(models.Model):
    username = models.CharField(max_length=100)
    current_company = models.CharField(max_length=100)
    desired_company = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.username
