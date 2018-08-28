from django.db import models

# Create your models here.


class Category(models.Model):
    category_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    category_index =  models.IntegerField()
class Question(models.Model):
    question_id =  models.CharField(max_length=200, primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE) 
    optinal = models.BooleanField(default=False)
    after = models.ManyToManyField("self", blank=True, null=True)
    question = models.CharField(max_length=200)
    answerType =  models.CharField(max_length=200)