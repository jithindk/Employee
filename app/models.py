from django.db import models
from django.contrib.auth.models import User





'''
class Skill(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    exp = models.IntegerField(null=True, blank=True, default=0)
    def __str__(self):
        return (self.name+'('+str(self.exp)+')')




class Employee(models.Model):

    GENDER = (
			('Male', 'Male'),
			('Female', 'Female'),
            ('Other', 'Other'),
			) 

    f_name = models.CharField(max_length=200, null=True)
    l_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER)
    skills = models.ManyToManyField(Skill)
    project = models.ManyToManyField(Project)
    
    def __str__(self):
        return (self.f_name+' '+self.l_name)
'''

class Employee(models.Model):
    
    GENDER = (
			('Male', 'Male'),
			('Female', 'Female'),
            ('Other', 'Other'),
			) 

    f_name = models.CharField(max_length=200, null=True)
    l_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER)
    skills = models.IntegerField(null=True, blank=True, default=0)
    projects = models.IntegerField(null=True, blank=True, default=0)
    def __str__(self):
        return self.f_name

class Skill(models.Model):
    employee = models.ForeignKey(Employee, null=True, on_delete= models.SET_NULL)
    S = models.CharField(max_length=200, null=True)
    exp = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.S

class Project(models.Model):
    employee = models.ForeignKey(Employee, null=True, on_delete= models.SET_NULL)
    P = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.P