# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=50)
    skills = models.ManyToManyField("Skill")
    employed = models.BooleanField()
    job_title = models.CharField(max_length=200)
    years_of_experience = models.IntegerField()
    seeking_titles = models.ManyToManyField("Title") 
       
class Question(models.Model):
    def as_dict(self):
        return self.question
          # other stuff
    question = models.CharField(max_length=300)

class Skill(models.Model):
    skill =  models.CharField(max_length=200, primary_key=True)
class Title(models.Model):
    title =  models.CharField(max_length=200, primary_key=True)
    