from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *
class Employee_Form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['f_name','l_name','gender','address']

        
        labels = {
            'f_name': "First Name",
            'l_name': 'Last Name',
            'gender': 'Gender',
            'address': 'Address',
        }

class Skill_Form(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

        labels = {
            'S': "Skill",
            'exp': 'Experience',
        }

class Project_Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

        labels = {
            'P': "Project",
        }
		

