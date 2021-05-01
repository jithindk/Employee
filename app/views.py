from django.shortcuts import render,redirect
from .filters import *
from .models import *
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .forms import *

# Create your views here.


def home(request):
    employee = Employee.objects.order_by('f_name')
    context = {'employee':employee}
    return render(request, 'app/home.html', context)


def Skill_Details(request):
    searchFilter = Filter_Skill(request.GET, queryset=Skill.objects.order_by('S','exp'))
    skill = searchFilter.qs
    employee = Employee.objects.all()
    project = Project.objects.all()
    emp_tot=0
    if len(skill)<=len(employee):
        emp_tot=len(skill)
    exp_tot=0
    for s in skill:
        exp_tot=exp_tot+s.exp
    context = {'searchFilter':searchFilter,'skill':skill,'project':project, 'employee':employee, 'exp_tot':exp_tot, 'emp_tot':emp_tot}
    return render(request, 'app/SkillFilter.html', context)


def Employee_Details(request, pk):
    employee = Employee.objects.get(id=pk)
    skills = employee.skill_set.all()
    project = employee.project_set.all()
    context = {'Employee':employee, "S":skills, "P":project}
    return render(request, 'app/Details/employee.html', context)


def Create_Employee(request):
    form = Employee_Form()

    if request.method == 'POST':
        form = Employee_Form(request.POST)
        if form.is_valid():
            form.save()
            employee = Employee.objects.latest('id')
            return redirect('employeeDetails', employee.id)

    context = {"form":form}
    return render(request, 'app/Forms/CreateEmployee.html', context)


def Update_Employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = Employee_Form(instance=employee)

    if request.method == 'POST':
        form = Employee_Form(request.POST, instance=employee)
        if form.is_valid:
            form.save()
            return redirect("employeeDetails", employee.id)

    context = {'form': form, 'item':employee.f_name, 'name':'Employee'}
    return render(request, 'app/Forms/update.html',context)



def Delete_Employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect("home")

    context = {'name':'Employee', 'item': employee}
    return render(request, 'app/Forms/delete.html',context)




def Create_Skill(request, pk):
    employee = Employee.objects.get(id=pk)
    form = Skill_Form(initial={'employee':employee})

    if request.method == 'POST':
        form = Skill_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeeDetails', employee.id)

    context = {"form":form, "Employee":employee}
    return render(request, 'app/Forms/CreateSkill.html', context)



def Update_Skill(request, pk):
    s = Skill.objects.get(id=pk)
    form = Skill_Form(instance=s)

    if request.method == 'POST':
        form = Skill_Form(request.POST, instance=s)
        if form.is_valid:
            form.save()
            return redirect("employeeDetails", s.employee.id)

    context = {'form': form, 'name':'Skill', 'item':"", 'skill':s}
    return render(request, 'app/Forms/update.html',context)



def Delete_Skill(request, pk):
    s = Skill.objects.get(id=pk)

    if request.method == 'POST':
        e = s.employee
        s.delete()
        return redirect("employeeDetails", e.id)

    context = {'name':'Skill', 'item': s.S}
    return render(request, 'app/Forms/delete.html',context)


def Create_Project(request, pk):
    employee = Employee.objects.get(id=pk)
    form = Project_Form(initial={'employee':employee})

    if request.method == 'POST':
        form = Project_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeeDetails', employee.id)

    context = {"form":form, "Employee":employee}
    return render(request, 'app/Forms/CreateProject.html', context)



def Update_Project(request, pk):
    p = Project.objects.get(id=pk)
    form = Project_Form(instance=p)

    if request.method == 'POST':
        form = Project_Form(request.POST, instance=s)
        if form.is_valid:
            form.save()
            return redirect("employeeDetails", p.employee.id)

    context = {'form': form, 'name':'Project', 'item':"",  'project':p}
    return render(request, 'app/Forms/update.html',context)



def Delete_Project(request, pk):
    p = Project.objects.get(id=pk)

    if request.method == 'POST':
        e = p.employee
        p.delete()
        return redirect("employeeDetails", e.id)

    context = {'name':'Project', 'item': p.P}
    return render(request, 'app/Forms/delete.html',context)




