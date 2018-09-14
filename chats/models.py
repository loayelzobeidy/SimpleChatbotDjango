

# Create your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from questions.models import Question
# Create your models here.
import uuid

class Skill(models.Model):
    skill =  models.CharField(max_length=200, primary_key=True)
    def __unicode__(self):
       return self.skill
    def __str__(self):
        return self.skill

    class Meta:
        ordering = ('skill',)
class Title(models.Model):
    title =  models.CharField(max_length=200, primary_key=True)
    def __unicode__(self):
       return self.title
    def as_dict(self):
         return dict((f.name, getattr(self, f.name)) for f in self._meta.fields)
class Switch_reasons (models.Model):
    reason =  models.CharField(max_length=200, primary_key=True)
    def __unicode__(self):
       return self.reason
    def as_dict(self):
         return dict((f.name, getattr(self, f.name)) for f in self._meta.fields)
class User(models.Model):
    email = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=50)
    skills = models.TextField(null=True)
    degree = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    graduation_year = models.CharField(max_length=50,default="2018")
    employement_status = models.CharField(max_length=200)
    current_occupation = models.CharField(max_length=200)
    industry_role = models.CharField(max_length=200)
    switch_reasons = models.TextField(null=True)
    # super_power = ListCharField(
    #     base_field=CharField(max_length=10),
    #     size=6,
    #     max_length=(6 * 11)  # 6 * 10 character nominals, plus commas
    # )
    employed = models.CharField(max_length=200,default="")
    job_title = models.CharField(max_length=200)
    years_of_experience = models.CharField(max_length=10,default=0)
    seeking_titles = models.TextField(null=True)
    gross_salary =  models.CharField(max_length=10,default=0)
    current_company_size =  models.CharField(max_length=200)
    def as_dict(self):
         return dict((f.name, str(getattr(self, f.name))) for f in self._meta.fields)
class Answer(models.Model):
    answer_id =  models.CharField(max_length=200, primary_key=True,default=uuid.uuid4())
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE,default=0)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    answer = models.CharField(max_length=1000)
    
class Session(models.Model):
    user_id = models.ForeignKey(User,on_delete=None)
    index_category= models.IntegerField()
    index_question= models.IntegerField()
    