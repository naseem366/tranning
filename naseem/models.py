from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.auth.models import User, Group


class EmpModel(models.Model):
    empid=models.CharField(max_length=20)
    empname=models.CharField(max_length=200)
    empemail=models.CharField(max_length=200)
    empphone=models.CharField(max_length=222)
    empdate=models.DateField()


class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    category_image=models.ImageField(default="",null=True,blank=True)
    def __str__(self):
         return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200,default='',null=True)
    region = models.CharField(default='',max_length=200, null=True)
    phone = models.CharField(default='',max_length=200, null=True)
    #username=models.CharField(default='',max_length=200,null=False)
    #email = models.CharField(default='',max_length=200, null=True)
    profile_pic = models.ImageField(default="o.png" ,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
@receiver(post_save,sender=User)
def customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
        print('profile created')

@receiver(post_save,sender=User)
def update_profile(sender,instance,created,**kwargs):
    if created ==False:
        instance.customer.save()
        print('profile update')


