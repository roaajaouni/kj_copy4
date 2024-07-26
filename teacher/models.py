from django.db import models
from django.contrib.auth.models import User,Group
import uuid
#from mother.models import Child
from django.db.models.signals import post_save
from django.dispatch import receiver
#from datetime import datetime


class Teacher(models.Model):
   
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
   

    def __str__(self):
        return str(self.user)



 
