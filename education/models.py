import email
from turtle import mode
from django.db import models

class users(models.Model):
    userID=models.AutoField
    fname=models.CharField(max_length=300)
    lname=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    password=models.CharField(max_length=300)

class Jobs(models.Model):
    JobID=models.AutoField
    Job_title=models.CharField(max_length=300)
    salary=models.IntegerField
    Description=models.CharField(max_length=300)
    skills_req=models.CharField(max_length=300)

class imag(models.Model):
    relative = models.CharField(max_length=100)
    image = models.FileField(upload_to='../images')