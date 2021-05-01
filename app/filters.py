from django.contrib.auth.models import User

from django.forms import CheckboxSelectMultiple
import django_filters

from .models import *

class Filter_Skill(django_filters.FilterSet):
    S = django_filters.CharFilter(field_name='S', lookup_expr='icontains')
    exp = django_filters.NumberFilter(field_name='exp',lookup_expr='gte')
    '''
    exp = django_filters.ModelMultipleChoiceFilter(
        queryset = Skill.objects.all(),
        widget = CheckboxSelectMultiple(),
        label = ' Skill: ',
    )
    '''
    class Meta:
        model = Skill
        fields = []

'''
class Filter_Employee(django_filters.FilterSet):
    #f_name = django_filters.CharFilter(field_name='f_name', lookup_expr='icontains')
    f_name = django_filters.ModelMultipleChoiceFilter(
        queryset = Employee.objects.all(),
        widget = CheckboxSelectMultiple(),
        label = ' Name: ',
    )
    
    class Meta:
        model = Employee
        fields = []
'''