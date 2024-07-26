from django.db import models
from django.contrib.auth.models import User,Group
# from teacher.models import Teacher,Report
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
from teacher.models import Teacher

class Mother(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
 

    def __str__(self):
        return str(self.user)



class Child(models.Model):
    meal_types = (('meat', 'meat'),
                  ('milk', 'milk'),
                  ('sandwich','sandwich'),
           ('nuggets','nuggets'),
            ('burger','burger'),
             ('pasta','pasta'),
               ('pie','pie'),
                 ('pizza','pizza'),
                  ('pancake','pancake'),
                   ('waffle','waffle'))
    meal_images = (
        ('meat','images/meat.jpg'),

        ('milk','images/milk.jpg'),
        ('sandwich', 'images/sandwich.jpg'),
        ('nuggets', 'images/nuggets.jpg'),
        ('burger', 'images/burger.jpg'),
        ('pasta', 'images/pasta.jpg'),
        ('pie', 'images/pie.jpg'),
        ('pizza', 'images/pizza.jpg'),
        ('pancake', 'images/pancake.jpg'),
        ('waffle', 'images/waffle.jpg')
        
    )
    gender = (
        ('male','Male'),
        ('female','Female')
    )
    a = (('5','5'),
         ('6','6'))
    lo = (('arrive','arrive'),
         ('left','left'))
    mom = models.ForeignKey(Mother,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True,blank=True)
    age = models.CharField(max_length=200,null=True,blank=True,choices=a)
    child_gender = models.CharField(max_length=200, null=True, blank=True, choices=gender)
    featured_image = models.ImageField(null=True,blank=True,upload_to='staticfiles/images/',default='default.png')
    meal = models.CharField(max_length=200, null=True, blank=True, choices=meal_types)
    notes = models.CharField(max_length=200,null=True,blank=True)
    state_health = models.CharField(max_length=200,null=True,blank=True)
    teach = models.ForeignKey(Teacher,null=True,blank=True,on_delete=models.SET_NULL)
    location = models.CharField(max_length=200,null=True,blank=True,choices=lo)
    created = models.DateTimeField(default = datetime.now)
    Important_notes = models.CharField(max_length=200, null=True, blank=True)
    meal_images_path = models.CharField(max_length=200, null=True, blank=True, choices=meal_images)

    def _str_(self):
        return str(self.name)
#تم التعديل اضافة صف التقرير وربط الطفل بالانسة 
  


class Report(models.Model):
    activity = (('drawing and coloring', 'drawing and coloring'),
                  ('music', 'music'),
                  ('reading stories','reading stories'))
   
    child = models.ForeignKey(Child,on_delete=models.CASCADE,null=True,blank=True)
    learn= models.CharField(max_length=200, null=True, blank=True)
    activities = models.CharField(max_length=200, null=True, blank=True,choices=activity)
    attiude = models.CharField(max_length=200,null=True,blank=True)
    mood= models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(default = datetime.now)
