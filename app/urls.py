from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),



    path('employeeDetails/<str:pk>', views.Employee_Details, name='employeeDetails'),

    path('skill/', views.Skill_Details, name='skillDetails'),

    path('createEmployee/', views.Create_Employee, name='createEmployee'),
    path('updateEmployee/<str:pk>', views.Update_Employee, name='updateEmployee'),
    path('deleteEmployee/<str:pk>', views.Delete_Employee, name='deleteEmployee'),

    path('createSkill/<str:pk>', views.Create_Skill, name='createSkill'),
    path('updateSkill/<str:pk>', views.Update_Skill, name='updateSkill'),
    path('deleteSkill/<str:pk>', views.Delete_Skill, name='deleteSkill'),

    path('createProject/<str:pk>', views.Create_Project, name='createProject'),
    path('updateProject/<str:pk>', views.Update_Project, name='updateProject'),
    path('deleteProject/<str:pk>', views.Delete_Project, name='deleteProject'),

]