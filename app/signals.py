from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import F
from .models import *


@receiver(post_save, sender=Project)
def Project_CountUP(sender, instance, created, **kwargs):
    if created:
        e = instance.employee
        e.projects=F('projects')+1
        e.save()

@receiver(post_delete, sender=Project)
def Skill_CountDown(sender, instance, **kwargs):
    e = instance.employee
    e.skills=F('skills')-1
    e.save()

@receiver(post_save, sender=Skill)
def Skill_CountUP(sender, instance, created, **kwargs):
    if created:
        e = instance.employee
        e.skills=F('skills')+1
        e.save()

@receiver(post_delete, sender=Skill)
def Skill_CountDown(sender, instance, **kwargs):
    e = instance.employee
    e.skills=F('skills')-1
    e.save()

@receiver(post_save, sender=Project)
def Project_CountUP(sender, instance, created, **kwargs):
    if created:
        e = instance.employee
        e.projct=F('project')+1
        e.save()

@receiver(post_delete, sender=Project)
def Skill_CountDown(sender, instance, **kwargs):
    e = instance.employee
    e.project=F('project')-1
    e.save()
