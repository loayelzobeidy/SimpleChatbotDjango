from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Category(models.Model):
    category_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    category_index =  models.IntegerField()
class Question(models.Model):
    question_id =  models.CharField(max_length=200, primary_key=True,default=uuid.uuid4())
    category = models.ForeignKey(Category,on_delete=models.CASCADE) 
    optinal = models.BooleanField(default=False)
    # after = models.ManyToManyField("self", blank=True, null=True,default=None)
    question = models.CharField(max_length=200)
    answerType =  models.CharField(max_length=200)
    className=models.CharField(max_length=200)
    after = models.TextField(null=True)
    priority = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(0)])
    owner =  models.CharField(max_length=200)
    def as_dict(self):
         return dict((f.name, getattr(self, f.name)) for f in self._meta.fields if f.name != 'category')
        # ,self.answerType,self.question_id,self.category,self.priority,self.optinal
          # other stuff
class PossibleAnswer(models.Model):
    answer_id =  models.CharField(max_length=200, primary_key=True,default=uuid.uuid4())
    question_id =  models.ForeignKey(Question,on_delete=models.CASCADE)
    answer =models.CharField(max_length=600)
    def as_dict(self):
         return self.answer
        