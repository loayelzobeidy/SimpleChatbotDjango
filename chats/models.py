

# Create your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from questions.models import Question
# Create your models here.

class Skill(models.Model):
    skill =  models.CharField(max_length=200, primary_key=True)
    def __str__(self):
        return self.skill

    class Meta:
        ordering = ('skill',)
class Title(models.Model):
    title =  models.CharField(max_length=200, primary_key=True)
    
class User(models.Model):
    email = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill)
    employed = models.BooleanField(default=False)
    job_title = models.CharField(max_length=200)
    years_of_experience = models.IntegerField(default=0)
    seeking_titles = models.ManyToManyField(Title) 
class Answer(models.Model):
    answer_id =  models.CharField(max_length=200, primary_key=True)
    # question_id = models.OneToOneField(Question,on_delete=None)
    user_id = models.OneToOneField(User,on_delete=None)
    answer = models.CharField(max_length=1000)
    
